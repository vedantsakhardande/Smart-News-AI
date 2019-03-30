def crawl(self, nGoalpages=10, ntotalPages=500, threshold=0.5,startURL, scorer=None) :
    pagesFound = 0
    ntotalPages = 0
    startpage = wikipage.Wikipage(startURL)
    scorer.score(startpage)
    heappush(self.queue, startpage)
    while pagesFound < npages and pagesCrawled < ntotalPages:
        nextpage = heappop(self.queue)
        if nextpage.score > threshold :
        self.pages.append(newpage)
        pagesFound += 1
    for link in nextpage.outwardLinks :
        newpage = wikipage.Wikipage(base+link)
        scorer.score(newpage)
        heappush(self.queue, newpage)
return self.pages