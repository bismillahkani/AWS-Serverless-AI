FROM public.ecr.aws/lambda/python:3.8

COPY clipcrop.py app.py requirements.txt ./
COPY model /opt/ml/model
COPY yolov5 /opt/ml/yolov5
COPY weights /opt/ml/weights

RUN yum update -y

RUN yum install git -y

RUN python3.8 -m pip install -r requirements.txt -t .

CMD ["app.lambda_handler"]
