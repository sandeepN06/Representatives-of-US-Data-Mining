import scrapy
import re

# https://www.house.gov/representatives

class WebCrawler(scrapy.Spider):
    name = 'webscraper'
    start_urls = ['https://www.house.gov/representatives']

    def parse(self, response):
        items = response.css('div.view-content')[1]
        names = items.css('a::text').getall()
        district = items.xpath('//td[contains(@class , "views-field views-field-value-3 views-field-value-4")]/text()').getall()
        party = items.xpath('//td[contains(@class , "views-field views-field-value-6")]/text()').getall()
        office_room = items.xpath('//td[contains(@class , "views-field views-field-value-7 views-field-value-8")]/text()').getall()
        phone = items.xpath('//td[contains(@class , "views-field views-field-value-9")]/text()').getall()
        committeeAssignment = items.xpath('//*[contains(@id,"housegov_reps_by_name")]/tbody/tr/td[6]').getall()
        CommitteeAssignment = []

        for representative in range(len(committeeAssignment)):
            print(representative)
            if len(committeeAssignment[representative]) == 95:
                CommitteeAssignment.append(" ")
            else:
                CommitteeAssignment.append(re.sub('<ul>|</ul>|<li>|</li>' , " ", committeeAssignment[representative][82:-13]))



        for (rep,dis,par,off,ph,committee) in zip(names,district,party,office_room,phone,CommitteeAssignment):

            first_name = rep.split(',')[0]
            last_name = rep.split(',')[1]
            district = dis[:len(dis)-8]
            party = par.replace(" ","")
            office_room = off[:len(off)-8]
            phone = ph[:len(ph)-8]
            committeeAssignment = committee

            yield {
                'first_name': first_name,
                'last_name':  last_name,
                'district':   district,
                'party':      party,
                'office_room': office_room,
                'phone':      phone,
                'type' : "Federal",
                'country' : "United State Of America",
                'committeeAssignment' : committeeAssignment

            }

            

# views-field views-field-value-3 views-field-value-4