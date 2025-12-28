#args

blog_1 = 'i am awesome'
blog_2 = 'cars '
blog_3 = 'picture'
site_title  = 'what'
def blog_posts(title,*args):
    print(title)
    for post in args:
        print(post)

blog_posts(site_title,blog_1, blog_2)

