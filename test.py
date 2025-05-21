



        


async def scraper(tusk):
    SBR_WS_CDP = 'wss://brd-customer-hl_f34fed3a-zone-scarperb:jd296i2tj89f@brd.superproxy.io:9222'  

    urls = []
    para = []


    api_key = 'AIzaSyCBnZlzXyKoX1ZSR94QcHPMl5Rd9NWl2fM'
    cx_id = '40c41cbde339248bf'




    #items = data.get('items', [])  
    #for item in items:
        #link = item.get('link')  
        #if link:
            #urls.append(link)
    #print(urls[5])

    searchm = genai.GenerativeModel('gemini-1.5-pro-latest', system_instruction="you create a singular prompt for google based on a task I give you. Keep it short and only foucs on the part of the task that requires a google search")
 


    async def scrape(scaler, page, data):


        items = data.get('items', [])

        if items:   
            #print('before')
            #print(scaler)
            urls.clear() 


            specific_url = items[scaler].get('link') 
            urls.append(specific_url)


        if specific_url:
            await page.goto(urls[0], timeout=2*60*1000) 
            html = await page.content()
            soup = BeautifulSoup(html, 'html.parser')
            paragraphs = [p.get_text() for p in soup.find_all('p')]
            if isinstance(paragraphs, list):
                paragraphs = "".join(paragraphs)
            para.append(paragraphs)



            #print(paragraphs)
            #print('after')
            #print(urls)






    async def run(pw, task):  
    

        search = searchm.generate_content(f'{task}')
        query = search.text
        url = f'https://www.googleapis.com/customsearch/v1?key={api_key}&cx={cx_id}&q={query}&num=3'



        response = requests.get(url)
        data = response.json()
        browser = await pw.chromium.connect_over_cdp(SBR_WS_CDP)  
        page = await browser.new_page()
        scaler = 0
        while scaler < 3:
            try:
                await scrape(scaler=scaler, page=page, data=data)
                scaler += 1
                #print('after')
                #print(scaler)
                #print(urls)

            except Exception as e:     
                scaler += 1
                #print('puppy')
                #print(scaler)zx
            finally:
                if scaler > 3:
                    await browser.close()
    
 
    async with async_playwright() as playwright:  
        await run(playwright, task=tusk)  
    info = ' '.join(para)
    return info