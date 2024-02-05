# LeagueSkinScrapper

LeagueSkinScrapper is a simple function used to download every splash art up to date from the page Wiki League of legends, what the project does is use the pages list of skin present
on the game and scrap every skin splash available

# To do:

-Create an Interface

# Notes:

-Currently the script seem to not be working, the reason why will be review soon and fixed when it's find. 
 ##UPDATE: The error was found and fixed properly. the issue in hands was a 403 Code (Forbbiden), the server return this because the way python was sending the request, to overcome this the following header must have to be added: 
 
 "{
          'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36',
  }"

This header bypass this problem emulating the way a browser would send a request fixing the issue, the same method will be use in another project that had the same problem.
