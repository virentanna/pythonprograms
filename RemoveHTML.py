import re
# as per recommendation from @freylis, compile once only
CLEANR = re.compile('<.*?>')

def cleanhtml(raw_html):
  cleantext = re.sub(CLEANR, '', raw_html)
  return cleantext

if __name__ == '__main__':
    # str1 = '<p>Dear Gino- Thank you so much for your kindness and patience, and for all of the effort you put into selling the house! We never could have made it all happen without you. Wishing you all the best--</p>'
    # str1 = '<p><span class="preserve-whitespace">AMAZING! Harriet was not only a fun person to see homes with, but she was so in tune to what we wanted in a home. She listened when we told her our priorities and she didn&#39;t have us running around looking at places that wouldn&#39;t interest us. She was very on board with my style and what i wanted our</span> <span class="minimize preserve-whitespace"> home to represent. Harriet gave great advice and suggestions as to what we could accomplish with our home as well.<br /><br />She&#39;s was 100% on our team when it came to negotiating and always wanted what was best for us. In the end, we closed on our dream home and we couldn&#39;t be happy to have had Harriet along side us every step of the way. Not only will she be our new neighbor, but she has become a friend! For anyone looking in the Armonk/Bedford area, in our opinion, there is no one else you should work with!</span>&nbsp;<a class="review-body-toggle yui3-toggle-content-link" id="yui_3_18_1_1_1453924278435_2501" rel="nofollow">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; </a></p>'
    # print(cleanhtml(str1))
