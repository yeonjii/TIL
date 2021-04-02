import hashlib
from django import template

 
register = template.Library()
 
 
@register.filter
def gravatar_url(email):
  return hashlib.md5(email.encode('utf-8').strip().lower()).hexdigest()