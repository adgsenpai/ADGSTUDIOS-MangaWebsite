#!/usr/bin/env python3


### Importing Modules, Files, etc...
from helper.chapter import *


### Getting Page info
class ChapterPage(CommonThings):

    def __init__(self, chapter_id, manga_id):
        """
        Object initialising
        chapter_id - int
        """

        self.chapID = chapter_id
        self.manga_id = manga_id
        super().__init__()    # Inheriting CommonThings class
        self.getPageUrl()        
        self.getChapterTitle()
    
    def getPageUrl(self):
        """
        Getting Url of all pages of requested chapters
        """
        self.requestToWeb(f'https://api.mangaowl.to/v1/chapters/{self.chapID}/images')

        jsonData = json.loads(self.webcontent)
        #save to file and indent    
        with open('page.json', 'w') as f:
            json.dump(jsonData, f, indent=4)
        resultData = jsonData['results']
        imgList = dict()
        count = 0

        for data in resultData:
            count += 1
            imgList[count] = data['image']
        self.pageList = json.dumps(imgList)

    def getChapterTitle(self):
        """
        Getting Chapter Title
        """
        self.requestToWeb(f'https://api.mangaowl.to/v1/stories/{self.manga_id}')

        jsonData = json.loads(self.webcontent)
        #save to file and indent
        chapters = jsonData['chapters']

        for chapter in chapters:
            if int(chapter['id']) == int(self.chapID):
                self.chapterTitle = chapter['name']
                break

        #find previous chapter
        for i in range(len(chapters)):
            if int(chapters[i]['id']) == int(self.chapID):
                if i == 0:
                    self.previousChapter = None
                    self.previousChapName = None                    
                else:
                    self.previousChapter = '/chapters/'+str(chapters[i-1]['id'])
                    self.previousChapName = chapters[i-1]['name']
                break
        
        #find next chapter
        for i in range(len(chapters)):
            if int(chapters[i]['id']) == int(self.chapID):
                if i == len(chapters)-1:
                    self.nextChapter = None
                    self.nextChapName = None
                else:
                    self.nextChapter =  '/chapters/'+str(chapters[i+1]['id'])
                    self.nextChapName = chapters[i+1]['name']
                break
        
        if not self.chapterTitle:
            self.chapterTitle = ''

        if not self.previousChapter:
            self.previousChapter = ''
    
        if not self.nextChapter:
            self.nextChapter = ''

        if not self.previousChapName:
            self.previousChapName = ''
        
        if not self.nextChapName:
            self.nextChapName = ''
            
        
        
