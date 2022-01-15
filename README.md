# Serverless AI Workshop

This repo contains source code and supporting files for the Serverless AI workshop.

It included the following folders:

- `/SAM/digit_classifier` - a serverless application for classifying handwritten digits using a machine learning model in PyTorch
- `/SAM/clip_crop` - a serverless application for searching and cropping objects in a image using YoloV5 and OpenAI CLIP
- `/Sagemaker/serverless_inference.ipynb` - jupyter notebook to deploy Huggingface sentiment classifier as Sagemaker serverless endpoint

### Prerequisite

- AWS account - [Create AWS account](https://www.youtube.com/watch?v=4C7KdLijj0E)
- AWS CLI - [Install the AWS CLI](https://docs.aws.amazon.com/cli/latest/userguide/getting-started-install.html)
- SAM CLI - [Install the SAM CLI](https://docs.aws.amazon.com/serverless-application-model/latest/developerguide/serverless-sam-cli-install.html)
- Docker - [Install Docker community edition](https://hub.docker.com/search/?type=edition&offering=community)

### SAM

SAM is Serverless Application Model to deploy serverless applications in AWS

In this workshop, we will deploy two applications. One is a simple mnist digit classifier and second one is little advanced that use Open AI CLIP and YoloV5 to search and crop objects in a image.

### SAM installation

1. Download SAM https://github.com/aws/aws-sam-cli/releases/latest/download/AWS_SAM_CLI_64_PY3.msi
2. Install SAM
3. Verify installation - Open cmd terminal and run `sam —version`

For more details : https://docs.aws.amazon.com/serverless-application-model/latest/developerguide/serverless-sam-cli-install-windows.html

### Serverless application deployment:

1. ` git clone --recursive https://github.com/bismillahkani/AWS-Serverless-AI.git`

2. Create IAM user with following permissions, 
   - IAMFullAccess
   - AWSLambda_FullAccess
   - AmazonAPIGatewayAdministrator
   - AWSCloudFormationFullAccess
   - AmazonEC2ContainerRegistryFullAccess
   - AmazonS3FullAccess
   - CloudWatchLogsFullAccess
   - AmazonEventBridgeFullAccess
   
3. IAM User access key - [Create access keys](https://docs.aws.amazon.com/powershell/latest/userguide/pstools-appendix-sign-up.html)

4. open terminal and run `aws configure`. Enter Access key and Secret key.

   ##### Digit Classifier application

5. `cd ~/SAM/digit_classifier`

6. open terminal and run `sam build`

7. run `sam deploy —guided` and follow the instructions as shown in terminal

8. Once deployed, copy the API url from Outputs and test it in POSTMAN`

   ##### Clip Crop application [Homework]

9. For clip_crop application, change directory `cd ~/SAM/clip_crop` 

10. Download the model weights for CLIP model from https://openaipublic.azureedge.net/clip/models/40d365715913c9da98579312b702a82c18be219cc2a73407c4526f58eba950af/ViT-B-32.pt and copy the weights to `/SAM/clip_crop/app/weights`

11. run `sam build` and `sam deploy --guided`

12. Once deployed, copy the API url of clip_crop from Outputs and update the `/SAM/clip_crop/app/testapi.py`

13. Run `testapi.py`

## Sagemaker serverless

1. Create a notebook instance in Sagemaker
2. Upload the serverless_inference.ipynb notebook
3. Run cell, deploy serverless endpoint and do inference

## Cost

I have not investigated the free tier usage for this workshop. Hence cannot guarantee that you will not be charged. You can refer the below AWS pricing details,

Lambda pricing - https://aws.amazon.com/lambda/pricing/

Sagemaker pricing - https://aws.amazon.com/sagemaker/pricing/

ECR pricing - https://aws.amazon.com/ecr/pricing/

API gateway pricing - https://aws.amazon.com/api-gateway/pricing/

## Clean-up

Don’t forget to delete all the resources you created for this workshop. Otherwise you will be charged.
