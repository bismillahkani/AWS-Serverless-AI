import tempfile

import clip
import torch


class ClipCrop():
    ''' Search and crop objects in the image '''

    def __init__(self):
        self.dirpath = tempfile.mkdtemp()
        self.yolo_model = torch.hub.load('/opt/ml/yolov5', 'custom', path='/opt/ml/weights/best.pt', source='local')
        self.device = "cuda" if torch.cuda.is_available() else "cpu"
        self.clip_model, self.clip_preprocess = clip.load("/opt/ml/weights/ViT-B-32.pt", device=self.device)

    def similarity_top(self, similarity_list, cropimage_list, N):
        ''' Find the similarity between the image and search query '''
        results = zip(range(len(similarity_list)), similarity_list)
        results = sorted(results, key=lambda x: x[1], reverse= True)
        top_images = []
        scores=[]
        for index,score in results[:N]:
            scores.append(score)
            top_images.append(cropimage_list[index])
        return scores,top_images,index
    
    def crop(self, image):
        ''' Crop the objects in image '''
        results = self.yolo_model(image)
        # save the crops in temp directory        
        results.crop(save_dir=self.dirpath)
        coords = results.xyxy[0].cpu().numpy()
        return coords
    
    def clip_embeddings(self,image, coords):
        ''' Get the embeddings of the objects in the image'''
        cropimage_list = [image.crop((xy[0],xy[1],xy[2],xy[3])) for xy in coords]
        images = torch.stack([self.clip_preprocess(im) for im in cropimage_list]).to(self.device)
        with torch.no_grad():
            clip_embeddings = self.clip_model.encode_image(images)
        clip_embeddings /= clip_embeddings.norm(dim=-1, keepdim=True)
        clip_embeddings.cpu().numpy()
        return clip_embeddings, cropimage_list
    
    def clip_crop(self,search_query,clip_embeddings,cropimage_list):
        ''' Crop the image similar to search queary '''
        with torch.no_grad():
            text_encoded = self.clip_model.encode_text(clip.tokenize(search_query).to(self.device))
            text_encoded /= text_encoded.norm(dim=-1, keepdim=True)
        similarity = text_encoded.cpu().numpy() @ clip_embeddings.cpu().numpy().T
        similarity = similarity[0]
        scores,imgs, index = self.similarity_top(similarity,cropimage_list,N=1)
        return scores,imgs,index
    
    def predict(self, image,search_query):
        ''' Clip crop inference pipeline '''
        # Step1: Crop the objects in the image
        coords = self.crop(image)
        # Step2: Get the embeddings of the objects in the image
        clip_embeddings, cropimage_list = self.clip_embeddings(image, coords)
        # Step3: Crop the image similar to search queary
        scores, imgs, index = self.clip_crop(search_query,clip_embeddings,cropimage_list)
        return scores,imgs,coords,index




