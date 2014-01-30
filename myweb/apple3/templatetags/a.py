from django import template
register=template.Library()
def check(value,arg):
	if value!=(arg-1):
		return 1
	else :
		return 0

def l(value,arg):
    return value[arg]

def times(value):
    	a=[range(value)]
	return a

def sm(value,arg):
    	return value+arg

def url(value):
    return value.image_urls

def cin(value,args):
    if value in args:
    	return 1
    else:
    	return 0

def pr(value):
    if(value=="Not available"):
    	return 0
    else:
    	return 1
def title(value):
    return value.title
def cost(value):
    return value.cost
def tdress(value):
    return value.type_dress
def tfab(value):
    return value.fabric
def tadvert(value):
    return value.advertiser
def timg(value):
    return value.image_urls
def tfit(value):
    return value.fit
def tcost(value):
    if(value.cost=="Not available"):
    	return "Not Availabe"
    else:
    	return value.cost
def cat(value):
    return value.category
def tcur(value):
    return value.currency
def tsize(value):
    val=value.size
    st=""
    i=0
    while i<len(val):
		if val[i]!=",":
			while val[i]!="," :
				st+=val[i]
				i+=1
				if i==len(val):
				    break
		st+=" "
		i+=1
    return st
def tcolor(value):
    val=value.color
    st=""
    i=0
    while i<len(val):
	if val[i]!=",":
		s=""
		while val[i]!=",":
			if s==" ":
				break
			s+=val[i]
			i+=1
			if i==len(val):
			    break
		if s!="Colour:":
		     st+=s
		     st+=" "
	i+=1
    return st
def source(value):
    return value.source
def pk(value):
    return value.pk
def chk(value):
    if value=="shoptiques":
    	return 1
    else:
    	return 0
def frcst(value):
    value=value.encode()
    st=""
    for i in value:
    	if i=='0' or  i=='1' or i=='2' or i=='3' or i=='4' or i=='5' or i=='6' or i=='7' or i=='8' or i=='9' or i=='.' :
    		st+=i
    return st
def nz(value):
    if value!=0:
    	return 1
    else:
    	return 0
def dval(value,args):
    one=value[args][0]
    sec=value[args][0]
    thr=value[args][0]
    s=""
    if one:
    	s+="Bodytags: "
    	for i in one:
    		s+=str(i)
    		s+=" "
    	s+=","
    if sec:
    	s+="Styletags: "
    	for i in sec:
    		s+=str(i)
    		s+=" "
    	s+=","
    if thr:
    	s+="Ocassiontags: "
    	for i in sec:
    		s+=str(i)
    		s+=" "
    return s
register.filter('times',check)
register.filter('cost',cost)
register.filter('chk',chk)
register.filter('tadvert',tadvert)
register.filter('timg',timg)
register.filter('tfab',tfab)
register.filter('tcost',tcost)
register.filter('tcur',tcur)
register.filter('tdress',tdress)
register.filter('tsize',tsize)
register.filter('tcolor',tcolor)
register.filter('tfit',tfit)
register.filter('source',source)
register.filter('cat',cat)
register.filter('title',title)
register.filter('l',l)
register.filter('pk',pk)
register.filter('sm',sm)
register.filter('url',url)
register.filter('check',check)
register.filter('frcst',frcst)
register.filter('pr',pr)
register.filter('nz',nz)
register.filter('cin',cin)
register.filter('dval',dval)
