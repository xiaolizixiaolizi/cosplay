# -*- coding: utf-8 -*-

# Define your item pipelines here
#
from  scrapy.pipelines.images import ImagesPipeline
from .settings import IMAGES_STORE
import  os
class CoserImagePipeline(ImagesPipeline):
    def  get_media_requests(self, item, info):
        request_objs=super(CoserImagePipeline,self).get_media_requests(item,info)
        for obj in request_objs:
            obj.item=item
        return  request_objs
    def file_path(self, request, response=None, info=None):
        path=super(CoserImagePipeline,self).file_path(request,response,info)
        category=request.item.get('title')
        images_store=IMAGES_STORE
        category_path=os.path.join(images_store,category)
        if not category_path:
            os.mkdir(category_path)
        image_name=path.replace('full/','')
        image_path=os.path.join(category_path,image_name)
        return  image_path










class CoserPipeline(object):
    def process_item(self, item, spider):
        return item
