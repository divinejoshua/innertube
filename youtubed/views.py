from django.shortcuts import render
from django.views import View
import pafy
import os
from django.template.defaultfilters import filesizeformat
#For the youtube video
import pytube
from django.http import FileResponse, Http404, HttpResponse


class homeView(View):
    template_name = 'index.html'
    context = {}

    def get(self, request):
        self.context ['get']  = "This is get"
        pwd = os.path.dirname(__file__)
        file_path = pwd + '/InnerTube_Video.mp4'
        if os.path.exists(file_path):
            os.remove(file_path)
        return render(request, self.template_name, self.context)





     


    def post(self, request):
        self.context ['post']  = "This is post"
        url = request.POST["link"]
        pwd = os.path.dirname(__file__)
        file_path = pwd + '/InnerTube_Video.mp4'
        if os.path.exists(file_path):
            os.remove(file_path)

        try:
            video = pytube.YouTube(url)			# Check if video
        except:
            return render(request, self.template_name, self.context)

        try:  
            # object creation using YouTube 
            # which was imported in the beginning 
            stream = video.streams.get_by_itag(22)
            print("downloading...")
            stream.download(os.path.dirname(__file__), filename="InnerTube_Video")
            

            file_path = pwd + '/InnerTube_Video.mp4'
            if os.path.exists(file_path):
                with open(file_path, 'rb') as fh:
                    response = HttpResponse(fh.read(), content_type="application/vnd.mp4")
                    response['Content-Disposition'] = 'inline; filename=' + os.path.basename(file_path)
                return response
            raise Http404
            self.context['message_r'] = "Downloaded"


          
            return render(request, self.template_name, self.context)


        except:  
            self.context['message_r'] = "Cannot download this video" #to handle exception  
            return render(request, self.template_name, self.context)


        return  FileResponse(open(file, 'rb'))
        return render(request, self.template_name, self.context)




# def home_screen_view(request, *args, **kwargs):
	
# 	context = {}

# 	# Search
# 	query = ""
# 	if request.GET:
# 		query = request.GET.get('q', '')
# 		context['query'] = str(query)

# 	blog_posts = sorted(get_blog_queryset(query), key=attrgetter('date_updated'), reverse=True)
	


# 	# Pagination
# 	page = request.GET.get('page', 1)
# 	blog_posts_paginator = Paginator(blog_posts, BLOG_POSTS_PER_PAGE)
# 	try:
# 		blog_posts = blog_posts_paginator.page(page)
# 	except PageNotAnInteger:
# 		blog_posts = blog_posts_paginator.page(BLOG_POSTS_PER_PAGE)
# 	except EmptyPage:
# 		blog_posts = blog_posts_paginator.page(blog_posts_paginator.num_pages)

# 	context['blog_posts'] = blog_posts

# 	return render(request, "personal/home.html", context)



