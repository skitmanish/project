from django.shortcuts import render,redirect
import requests
import wikipedia
from bs4 import BeautifulSoup
from googletrans import Translator
from django.shortcuts import render,redirect,get_object_or_404
from guide.models import Guide
from ticket.models import Ticket
from geopy.geocoders import Nominatim
import random

destination=['en']

def detail(request,place_id):
    de1='Nahargarh Fort'
    de2='lake palace rajasthan'

    if place_id==302:
        url='https://en.wikipedia.org/wiki/Hawa_Mahal'
        de='Hawa_Mahal'
        de1='Hawa Mahal, Neer Sagar Market, Bhakrota, Jaipur, Rajasthan'
        de2='Hawa Mahal jaipur'

    if place_id==303:
        url='https://en.wikipedia.org/wiki/Rambagh_Palace'
        de='Rambagh_Palace'
        de1='Rambagh Palace, Jaipur, Bhawani Singh Road, Jaipur, Rajasthan'
        de2='Rambagh Palace rajasthan'

    if place_id==304:
        url='https://en.wikipedia.org/wiki/Devi_Garh_Palace'
        de='Devi_Garh_Palace'
        de1='RAAS Devigarh, Udaipur, Rajasthana'
        de2='udaipur'

    if place_id==305:
        url='https://en.wikipedia.org/wiki/Jag_Mandir'
        de='Jag_Mandir'
        de2='Jag Mandir'
        de1='Jag Mandir, Rampura, Kota, Rajasthan'

    if place_id==306:
        url='https://en.wikipedia.org/wiki/City_Palace,_Udaipur'
        de='City_Palace,_Udaipur'
        de1='City Palace, Old City, Udaipur, Rajasthan'
        de2='City Palace Udaipur'
    if place_id==307:
        url='https://en.wikipedia.org/wiki/Chittor_Fort'
        de='Chittor_Fort'
        de1='Chittorgarh Fort, Chittorgarh, Rajasthan'
        de2='Chittor Fort'

    if place_id==308:
        url='https://en.wikipedia.org/wiki/Ranthambore_Fort'
        de='Ranthambore_Fort'
        de1='Ranthambore Fort, Sawai Madhopur, Rajasthan'
        de2='Ranthambore Fort'
    if place_id==309:
        url='https://en.wikipedia.org/wiki/Gagron_Fort'
        de='Gagron_Fort'
        de2='Gagron Fort'
        de1='Gagron Fort, Gagron, Rajasthan'
    if place_id==310:
        url='https://en.wikipedia.org/wiki/Amber_Fort'
        de='Amber_Fort'
        de2='Amber Fort'
        de1='Arya Samaj Road, Gurjar Mohalla, Tara Mahendra Colony, Bharatpur, Rajasthan'
    if place_id==311:
        url='https://en.wikipedia.org/wiki/Jaisalmer_Fort'
        de='Jaisalmer_Fort'
        de2='Jaisalmer Fort'
        de1='Jaisalmer Fort, Dhibba Para, Manak Chowk, Amar Sagar Pol, Jaisalmer, Rajasthan'
    if place_id==312:
        url='https://en.wikipedia.org/wiki/Kumbhalgarh_Fort'
        de='Kumbhalgarh_Fort'
        de2='Kumbhalgarh Fort'
        de1='Kumbhalgarh Fort, Kumbhalgarh, Rajasthan'
    if place_id==313:
        url='https://en.wikipedia.org/wiki/Mehrangarh_Fort'
        de='Mehrangarh_Fort'
        de2='Mehrangarh Fort'
        de1='Mehrangarh Fort Museum, The Fort, Paota, Jodhpur, Rajasthan'
    if place_id==314:
        url='https://en.wikipedia.org/wiki/Nahargarh_Fort'
        de='Nahargarh_Fort'
        de2='Nahargarh Fort jaipur'
        de1='Nahargarh Fort, Krishna Nagar, Brahampuri, Jaipur, Rajasthan'
    if place_id==315:
        url='https://en.wikipedia.org/wiki/Bhatner_fort'
        de='Bhatner_fort'
        de2='Bhatner fort'
        de1='Bhatner Fort, Hanumangarh, Rajasthan'
    if place_id==316:
        url='https://en.wikipedia.org/wiki/Junagarh_Fort'
        de='Junagarh_Fort'
        de2='Junagarh Fort'
        de1='Junagarh Fort, Bikaner Fort, Bikaner, Rajasthan'
    if place_id==317:
        url='https://en.wikipedia.org/wiki/Lohagarh_Fort'
        de='Lohagarh_Fort'
        de2='Lohagarh Fort'
        de1='Lohagarh Fort, Lohagarh Fort, Gopalgarh, Bharatpur, Rajasthan'
    if place_id==318:
        url='https://en.wikipedia.org/wiki/Taragarh_Fort,_Ajmer'
        de='Taragarh_Fort,_Ajmer'
        de1='Taragarh Fort, Taragarh Road, Taragarh, Ajmer, Rajasthan'
        de2='Tara garh Ajmer'

    if place_id==319:
        url='https://en.wikipedia.org/wiki/Jalore_Fort'
        de='Jalore_Fort'
        de2='Jalore Fort'
        de1='Jalore Fort, Jalore, Rajasthan'
    if place_id==320:
        url='https://en.wikipedia.org/wiki/Nagaur#Tourism'
        de='Nagaur Tourism'
        de2='Nagaur'
        de1='Nagaur Fort, Bhandariyon Ki Gali, Nagaur, Rajasthan'
    if place_id==321:
        url='https://en.wikipedia.org/wiki/Dholpur#Tourism_and_landmarks'
        de='Dholpur#Tourism_and_landmarks'
        de2='Dholpur'
        de1='Dholpur, Rajasthan'
    if place_id==322:
        url='https://en.wikipedia.org/wiki/Ajmer_Jain_temple'
        de='Ajmer_Jain_temple'
        de1='Digamber Jain Temple, Dumada, Adarsh Nagar, Ajmer, Rajasthan'
        de2='Ajmer Jain temple'
    if place_id==323:
        url='https://en.wikipedia.org/wiki/Laxmi_Niwas_Palace'
        de='Laxmi_Niwas_Palace'
        de2='Laxmi Niwas Palace'
        de1='Laxmi Niwas Palace '
    if place_id==324:
        url='https://en.wikipedia.org/wiki/Vijaya_Stambha'
        de='Vijaya_Stambha'
        de1='Vijaya Stambha, Chittorgarh Fort Village, Chittorgarh, Rajasthan'
        de2='Vijaya Stambha'
    if place_id==325:
        url='https://en.wikipedia.org/wiki/Jal_Mahal'
        de='Jal_Mahal'
        de1='Jal Mahal, Amer Road, Jal Mahal, Amer, Jaipur, Rajasthan'
        de2='Jal Mahal'



    if place_id==327:
        url='https://en.wikipedia.org/wiki/Jaswant_Thada'
        de='Jaswant_Thada'
        de2='jodhpur'
        de1='Jaswant Thada, Lawaran, Jodhpur, Rajasthan'

    if place_id==328:
        url='https://en.wikipedia.org/wiki/Dilwara_Temples'
        de='Dilwara_Temples'
        de1='Dilwara Temples, Delwara, Mount Abu, Rajasthan'

    if place_id==329:
        url='https://en.wikipedia.org/wiki/Pushkar_lake'
        de='Pushkar_lake'
        de1='Pushkar Lake, Pushkar, Rajasthan'
        de2='Pushkar lake'
    if place_id==330:
        url='https://en.wikipedia.org/wiki/Ranakpur_Jain_Temple'
        de='Ranakpur_Jain_Temple'
        de1='Ranakpur Jain Temple, Ranakpur Road, Sadri, Rajasthan'
        de2='Sadri'

    if place_id==331:

        url='https://en.wikipedia.org/wiki/Ranthambore_National_Park'
        de='Ranthambore_National_Park'
        de1='Ranthambore National Park, Rajasthan'
        de2='Ranthambore park'

    if place_id==332:
        url='https://en.wikipedia.org/wiki/Shekhawati'
        de='Shekhawati'
        de1='Shekhawati, Rajasthan'
        de2='Shekhawati'
    if place_id==333:
        url='https://en.wikipedia.org/wiki/City_Palace,_Jaipur'
        de='City palace Jaipur'
        de1='City Palace, Tulsi Marg, Gangori Bazaar, J.D.A. Market, Pink City, Jaipur, Rajasthan'
        de2='City palace Jaipur'
    if place_id==334:
        url='https://en.wikipedia.org/wiki/Govind_Dev_Ji_Temple'
        de='Govind_Dev_Ji_Temple'
        de1='Govind Devji Temple Jaipur, Jai Niwas Garden, Gangori Bazaar, J.D.A. Market, Pink City, Jaipur, Rajasthan'
        de2='Govind Dev Ji jaipur'
    if place_id==335:
        url='https://en.wikipedia.org/wiki/Albert_Hall_Museum'
        de='Albert_Hall_Museum'
        de1='Albert Hall Museum, Jaipur, Rajasthan'
        de2='Albert Hall Museum jaipur'

    if place_id==337:
        url='https://en.wikipedia.org/wiki/Padampura'
        de='Padampura Jaipur'
        de1='Padampura, Jaipur, Rajasthan'
        de2='Padampura Jaipur'
    if place_id==338:
        url='https://en.wikipedia.org/wiki/Sanganer'
        de='Sanganer jaipur'
        de1='Sanganer, Jaipur, Rajasthan'
        de2='Sanganer jaipur'
    if place_id==339:
        url='https://en.wikipedia.org/wiki/Raj_Mandir_Cinema,_Jaipur'
        de='Raj_Mandir_Cinema,Jaipur'
        de1='Raj Mandir, Bhagwan Das Road, Panch Batti, C Scheme, Ashok Nagar, Jaipur, Rajasthan'
        de2='rajmandir jaipur'
    if place_id==340:
        url='https://en.wikipedia.org/wiki/World_Trade_Park,_Jaipur'
        de='World Trade_Park,Jaipur'
        de1='World Trade Park, Jaipur, Jawahar Lal Nehru Marg, Malviya Nagar, Jaipur, Rajasthan'
        de2='JLN circle jaipur'
    if place_id==341:
        url='https://en.wikipedia.org/wiki/Jantar_Mantar,_Jaipur'
        de='Jantar_Mantar,Jaipur'
        de1='Jantar Mantar, Gangori Bazaar, J.D.A. Market, Pink City, Jaipur, Rajasthan'
        de2='Jantar Mantar Jaipur'

    if place_id==1:

            url='https://en.wikipedia.org/wiki/Zoological_Garden,_Alipore'
            de='Zoological Garden, Alipore'
            de1='Zoological Garden Alipore, Alipore Road, Alipur Zoological Garden, Alipore, Kolkata, West Bengal'
            de2='Alipore Zoo'

    if place_id==5:
            url='https://en.wikipedia.org/wiki/Indira_Gandhi_Zoological_Park'
            de='Indira Gandhi Zoological Park'
            de1='Indira Gandhi Zoological Park, Visakhapatnam, Andhra Pradesh'
    if place_id==6:
            url='https://en.wikipedia.org/wiki/National_Zoological_Park_Delhi'
            de='National Zoological Park Delhi'
            de1='National Zoological Park, Sundar Nagar, New Delhi, Delhi'

    if place_id==12:
            url='https://en.wikipedia.org/wiki/Ana_Sagar_Lake'
            de='Ana Sagar Lake'
            de1='Ana Sagar Lake, Ajmer, Rajasthan'


    if place_id==37:
            url='https://en.wikipedia.org/wiki/Kumbhalgarh'
            de='Kumbhalgarh'
            de1='Kumbhalgarh, Rajasthan'
    if place_id==38:
            url='https://en.wikipedia.org/wiki/Mehrangarh'
            de='Mehrangarh'
            de1='Mehrangarh Fort and Museum, The Fort, Paota, Jodhpur, Rajasthan'

    if place_id==40:
            url='https://en.wikipedia.org/wiki/Vijaygarh_Fort'
            de='Vijaygarh Fort'
            de1='Vijaygarh Fort, Robertsganj, Uttar Pradesh'
    #<!--Rivers in India-->

    if place_id==44:
            url='https://en.wikipedia.org/wiki/Bhagirathi_River'
            de='Bhagirathi River'
            de1='Bhagirathi River, Gangotri, Uttarakhand'
    if place_id==45:
            url='https://en.wikipedia.org/wiki/Ganges'
            de='Ganges'
            de1='ganga river varanasi'
    if place_id==84:
            url='https://en.wikipedia.org/wiki/Eden_Gardens'
            de='Eden Gardens'
            de1='Eden Gardens, Kolkata, West Bengal'



    if place_id==88:
            url='https://en.wikipedia.org/wiki/Netaji_Indoor_Stadium'
            de='Netaji Indoor Stadium'
            de1='Netaji Indoor Stadium, Strand Road, Kolkata, West Bengal'
    if place_id==201:
        url='https://en.wikipedia.org/wiki/Abujmarh'
        de='Abujmarh'
        de1='Abujmarh, Narayanpur, Chhattisgarh'
    if place_id==221:
        url='https://en.wikipedia.org/wiki/Ajanta_Caves'
        de='Ajanta Caves'
        de1='Ajanta Caves, Maharashtra'

    if place_id==222:
        url='https://en.wikipedia.org/wiki/Ellora_Caves'
        de='Ellora Caves'
        de1='Ellora Caves, Ellora Cave Road, Ellora, Maharashtra'

    if place_id==223:
        url='https://en.wikipedia.org/wiki/Agra_Fort'
        de='Agra Fort'
        de1='Agra Fort, Agra Fort, Rakabganj, Agra, Uttar Pradesh'

    if place_id==224:
        url='https://en.wikipedia.org/wiki/Taj_Mahal'
        de='Taj Mahal'
        de1='Taj Mahal, Dharmapuri, Forest Colony, Tajganj, Agra, Uttar Pradesh'



    if place_id==225:
        url='https://en.wikipedia.org/wiki/Sun_Temple,_Kon%C3%A2rak'
        de='Sun Temple, Konârak'
        de1='Sun Temple, Konark, Odisha'



    if place_id==227:
        url='https://en.wikipedia.org/wiki/Kaziranga_National_Park'
        de='Kaziranga National Park'
        de1='Kaziranga National Park, Kanchanjuri, Assam'

    if place_id==228:
        url='https://en.wikipedia.org/wiki/Manas_Wildlife_Sanctuary'
        de='Manas Wildlife Sanctuary'
        de1='wildlife sanctuary near Manas National Park, Gobardhana, Assam'


    if place_id==229:
        url='https://en.wikipedia.org/wiki/Keoladeo_National_Park'
        de='Keoladeo National Park'
        de1='Keoladeo National Park, Bharatpur, Rajasthan'

    if place_id==230:
        url='https://en.wikipedia.org/wiki/Churches_and_Convents_of_Goa'
        de='Churches and Convents of Goa'
        de1='Immaculate Conception Church'

    if place_id==231:
        url='https://en.wikipedia.org/wiki/Khajuraho_Group_of_Monuments'
        de='Khajuraho Group of Monuments'
        de1='Khajuraho Group of Monuments, Madhya Pradesh'

    if place_id==232:
        url='https://en.wikipedia.org/wiki/Group_of_Monuments_at_Hampi'
        de='Group of Monuments at Hampi'
        de1='Group of Monuments at Hampi, Hampi, Karnataka'

    if place_id==233:
        url='https://en.wikipedia.org/wiki/Fatehpur_Sikri'
        de='Fatehpur Sikri'
        de1='Fatehpur Sikri, Uttar Pradesh'

    if place_id==234:
        url='https://en.wikipedia.org/wiki/Pattadakal'
        de='Group of Monuments at Pattadakal'
        de1='Group of Monuments at Pattadakal, UNESCO World Heritage Site, Pattadakal, Karnataka'

    if place_id==235:
        url='https://en.wikipedia.org/wiki/Elephanta_Caves'
        de='Elephanta Caves'
        de1='Elephanta Caves, Gharapuri, Maharashtra'

    if place_id==236:
        url='https://en.wikipedia.org/wiki/Great_Living_Chola_Temples'
        de='Great Living Chola Temples'
        de1='Great living chola temples, Karnataka'

    if place_id==237:
        url='https://en.wikipedia.org/wiki/Darasuram'
        de='Airavateshwarar Temple, Darasuram, Tamil Nadu, India'
        de1='airavateswarar temple in tirupur'

    if place_id==238:
        url='https://en.wikipedia.org/wiki/Brihadeeswarar_Temple'
        de='Brihadeeswarar Temple, Thanjavur, Tamil Nadu, India'
        de1='Brihadeeswara Temple, Membalam Road, Balaganapathy Nagar, Thanjavur, Tamil Nadu, India'

    if place_id==239:
        url='https://en.wikipedia.org/wiki/Sundarbans_National_Park'
        de='Sundarbans National Park'
        de1='Sundarban National Park, Kolkata, West Bengal'

    if place_id==240:
        url='https://en.wikipedia.org/wiki/Nanda_Devi_and_Valley_of_Flowers_National_Parks'
        de='Nanda Devi and Valley of Flowers National Parks'
        de1='nanda devi and valley of flowers national parks'

    if place_id==241:
        url='https://en.wikipedia.org/wiki/Buddhist_Monuments_at_Sanchi'
        de='Buddhist Monuments at Sanchi'
        de1='Sanchi, Madhya Pradesh'

    if place_id==242:
        url='https://en.wikipedia.org/wiki/Humayun%27s_Tomb'
        de='Humayun\'s Tomb, Delhi'
        de1='Humayun’s Tomb, Nizamuddin, Nizamuddin East, New Delhi, Delhi'

    if place_id==243:
        url='https://en.wikipedia.org/wiki/Qutb_complex'
        de='Qutub Minar and its Monuments, Delhi'
        de1='Qutub Minar Complex, Seth Sarai, Mehrauli, New Delhi, Delhi'

    if place_id==244:
        url='https://en.wikipedia.org/wiki/Mountain_railways_of_India'
        de='Mountain Railways of India'
        de1='Darjeeling Himalayan Railway, West Bengal, India, Darjeeling Himalayan Railway, Mahanadi Tea Garden, West Bengal'

    if place_id==245:
        url='https://en.wikipedia.org/wiki/Nilgiri_Mountain_Railway'
        de='Nilgiri Mountain Railway (2005) Ooty, Tamil Nadu, India'
        de1='Ooty, Tamil Nadu, India'

    if place_id==246:
        url='https://en.wikipedia.org/wiki/Kalka-Shimla_Railway'
        de='Kalka-Shimla Railway, Himachal Pradesh (2008)India'
        de1='Kalka - Shimla Road, Housing Board Colony, Kalka, Haryana'

    if place_id==247:
        url='https://en.wikipedia.org/wiki/Mahabodhi_Temple_Complex_at_Bodh_Gaya'
        de='Mahabodhi Temple Complex at Bodh Gaya'
        de1='Mahabodhi Temple, Bodh Gaya, Bihar'

    if place_id==248:
        url='https://en.wikipedia.org/wiki/Rock_Shelters_of_Bhimbetka'
        de='Rock Shelters of Bhimbetka'
        de1='rock shelters of bhimbetka'

    if place_id==249:
        url='https://en.wikipedia.org/wiki/Chhatrapati_Shivaji_Terminus'
        de='Chhatrapati Shivaji Terminus (formerly Victoria Terminus)'
        de1='Chhatrapati Shivaji Terminus Area, Fort, Mumbai, Maharashtra'

    if place_id==250:
        url='https://en.wikipedia.org/wiki/Champaner-Pavagadh_Archaeological_Park'
        de='Champaner-Pavagadh Archaeological Park'
        de1='Champaner-Pavagadh Archaeological Park, Champaner, Gujarat'

    if place_id==251:
        url='https://en.wikipedia.org/wiki/Red_Fort'
        de='Red Fort Complex'
        de1='Red Fort, Netaji Subhash Marg, Lal Qila, Chandni Chowk, New Delhi, Delhi'

    if place_id==252:
        url='https://en.wikipedia.org/wiki/Jantar_Mantar,_Jaipur'
        de='The Jantar Mantar, Jaipur'
        de1='The Jantar Mantar, Jaipur'

    if place_id==253:
        url='https://en.wikipedia.org/wiki/Western_Ghats'
        de='Western Ghats'
        de1='Western Ghats'

    if place_id==254:
        url='https://en.wikipedia.org/wiki/Periyar_National_Park'
        de='Periyar Sub-Cluster'
        de1='Periyar River, Kerala'

    if place_id==255:
        url='https://en.wikipedia.org/wiki/Anamalai_Mountains'
        de='Anamalai Sub-Cluster'
        de1='Anamalai Tiger Reserve, Pollachi, Tamil Nadu'

    if place_id==256:
        url='https://en.wikipedia.org/wiki/Nilgiri_mountains'
        de='Nilgiri Sub-Cluster'
        de1='Nilgiris, Tamil Nadu'

    if place_id==257:
        url='https://en.wikipedia.org/wiki/Talakaveri_Wildlife_Sanctuary'
        de='Talakaveri Sub-Cluster (five properties)'
        de1='Talakaveri, Karnataka'

    if place_id==258:
        url='https://en.wikipedia.org/wiki/Kudremukh'
        de='Kudremukh Sub-Cluster (five properties)'
        de1='Kudremukh, Karnataka'

    if place_id==259:
        url='https://en.wikipedia.org/wiki/Sahyadri_Mountains'
        de='Sahyadri Sub-Cluster'
        de1='Sahyādri, Kannan Devan Hills, Kerala'

    if place_id==260:
        url='https://en.wikipedia.org/wiki/Hill_Forts_of_Rajasthan'
        de='Hill Forts of Rajasthan'
        de1='Rajasthan'

    if place_id==261:
        url='https://en.wikipedia.org/wiki/Kumbhalgarh'
        de='Kumbhalgarh'
        de1='Kumbhalgarh Fort, Kumbhalgarh, Rajasthan'

    if place_id==262:
        url='https://en.wikipedia.org/wiki/Ranthambhore_Fort'
        de='Ranthambhore'
        de1='Ranthambore Fort, Sawai Madhopur, Rajasthan'

    if place_id==263:
        url='https://en.wikipedia.org/wiki/Amber_Fort'
        de='Amber Sub-Cluster'
        de1='Amber Palace, Amer, Jaipur, Rajasthan'

    if place_id==264:
        url='https://en.wikipedia.org/wiki/Jaisalmer_Fort'
        de='Jaisalmer'
        de1='Jaisalmer Fort, Jaisalmer, Rajasthan'

    if place_id==265:
        url='https://en.wikipedia.org/wiki/Gagron_Fort'
        de='Gagron'
        de1='Gagron Fort, Gagron, Rajasthan'

    if place_id==266:
        url='https://en.wikipedia.org/wiki/Rani_ki_vav'
        de='Rani ki vav (The Queen\'s Stepwell)'
        de1='Rani Ki Vav, Mohan Nagar Socity, Patan, Gujarat'

    if place_id==267:
        url='https://en.wikipedia.org/wiki/Great_Himalayan_National_Park'
        de='Great Himalayan National Park'
        de1='Great Himalayan National Park, Forest Office Road, Shamshi, Himachal Pradesh'

    if place_id==268:
        url='https://en.wikipedia.org/wiki/Nalanda'
        de='Archaeological Site of Nalanda Mahavihara at Nalanda, Bihar'
        de1='archaeological site of nalanda mahavihara at nalanda bihar'

    if place_id==269:
        url='https://en.wikipedia.org/wiki/Khangchendzonga_National_Park'
        de='Khangchendzonga National Park'
        de1='Khangchendzonga National Park, Sikkim'


    if place_id==271:
        url='https://en.wikipedia.org/wiki/Historic_City_of_Ahmadabad'
        de='Historic City of Ahmedabad'
        de1='Ahmedabad, Gujarat'

    if place_id==272:
        url='https://en.wikipedia.org/wiki/The_Victorian_and_Art_Deco_Ensemble_of_Mumbai'
        de='The Victorian and Art Deco Ensemble of Mumbai'
        de1='The Victorian and Art Deco Ensemble of Mumbai, Mantralaya, Fort, Mumbai, Maharashtra'


    try:
        answer = wikipedia.summary(de,sentences=10)
    except:
        answer='not found'
    print(de)



    translator = Translator()
    o=translator.translate(answer,dest=destination[0])
    #if destination[0]!='en':
    #    o1=translator.translate(de,dest=destination[0])
    #    m1=o1.text
    #else:
    #    m1=de
    fre=[]
    page=requests.get(url).text
    soup=BeautifulSoup(page,'html.parser')
    body=soup.find('body')
    conten=body.find('div',id='content')
    conten1=conten.find('div',id='bodyContent')
    conten2=conten1.find('div',id='mw-content-text')
    conten3=conten2.find('div',class_='mw-parser-output')
    op=conten3.find_all('div',class_='thumb tright')
    op=op+conten3.find_all('div',class_='thumb tleft')
    op=op+conten3.find_all('div',class_='thumb tmulti tright')
    table=conten3.find('table',class_="infobox vcard")
    if table==None:
        table=conten3.find('table',class_="infobox geography vcard")
    if table!=None:
        table1=table.find('img')
        table2=table1['src']
        table3='http:'+table2

        table4=de
        fre=[(table3,table4)]



    gallery=conten3.find('ul',class_='gallery mw-gallery-packed')
    items=[]
    items=op
    if gallery==None:
        gallery=conten3.find('ul',class_='gallery mw-gallery-traditional')
    if gallery==None:
        gallery=conten3.find('ul',class_='gallery mw-gallery-packed-hover')
    if gallery==None:
        gallery=conten3.find('ul',class_='gallery mw-gallery-traditional center')
    if gallery!=None:
        items=items+gallery.find_all(class_='gallerybox')
    var=de1.split(' ')
    for i in range(0,len(var)):
        var1=var[i].split(',')
    #print(var1)

    url='https://maps.google.com/maps?q='
    for i in range(0,len(var)):
        if i!=len(var)-1:
            url=url+var[i]+'%20'
        else:
            url=url+var[i]


    url=url+'&t=&z=13&ie=UTF8&iwloc=&output=embed'
    print(url)

    for i in range(0,len(items)):
        result=items[i].find('img')
        re=result['src']
        re='http:'+re
        re1=items[i].find('div',class_='gallerytext')
        if re1==None:
            re1=items[i].find('div',class_='thumbcaption')
        re1=re1.text
        re1=re1.replace('\n','')
        re1=translator.translate(re1,dest=destination[0])
        re1=re1.text
        fre=fre+[(re,re1)]

    id=()
    for i in range(0,10):
            it=()
            it=(random.randint(6,10),)
            if it not in id:
                if len(id)<3:
                    id=(id+it)
    print(id)
    guides=Guide.objects.filter(id__in=id)


    return render(request,'place/detail.html',{'images':fre,'ans':o.text,'title':de,'place_id':place_id,'url':url,'guides':guides})

def lang(request,lan_id,place_id):
    if lan_id==0:
        destination[0]='en'
    if lan_id==1:
        destination[0]='af'
    if lan_id==2:
        destination[0]='sq'
    if lan_id==3:
        destination[0]='ar'
    if lan_id==4:
        destination[0]='az'
    if lan_id==5:
        destination[0]='eu'
    if lan_id==6:
        destination[0]='bn'
    if lan_id==7:
        destination[0]='be'
    if lan_id==8:
        destination[0]='bg'
    if lan_id==9:
        destination[0]='ca'
    if lan_id==10:
        destination[0]='zh-CN'
    if lan_id==11:
        destination[0]='zh-TW'
    if lan_id==12:
        destination[0]='hr'
    if lan_id==13:
        destination[0]='cs'
    if lan_id==14:
        destination[0]='da'
    if lan_id==15:
        destination[0]='nl'
    if lan_id==16:
        destination[0]='eo'
    if lan_id==17:
        destination[0]='et'
    if lan_id==18:
        destination[0]='tl'
    if lan_id==19:
        destination[0]='fi'
    if lan_id==20:
        destination[0]='fr'
    if lan_id==21:
        destination[0]='gl'
    if lan_id==22:
        destination[0]='ka'
    if lan_id==23:
        destination[0]='de'
    if lan_id==24:
        destination[0]='el'
    if lan_id==25:
        destination[0]='gu'
    if lan_id==26:
        destination[0]='ht'
    if lan_id==27:
        destination[0]='iw'
    if lan_id==28:
        destination[0]='hi'
    if lan_id==29:
        destination[0]='hu'
    if lan_id==30:
        destination[0]='is'
    if lan_id==31:
        destination[0]='id'
    if lan_id==32:
        destination[0]='ga'
    if lan_id==33:
        destination[0]='it'
    if lan_id==34:
        destination[0]='ja'
    if lan_id==35:
        destination[0]='kn'
    if lan_id==36:
        destination[0]='ko'
    if lan_id==37:
        destination[0]='la'
    if lan_id==38:
        destination[0]='lb'
    if lan_id==39:
        destination[0]='lt'
    if lan_id==40:
        destination[0]='mk'
    if lan_id==41:
        destination[0]='ms'
    if lan_id==42:
        destination[0]='mt'
    if lan_id==43:
        destination[0]='no'
    if lan_id==44:
        destination[0]='fa'
    if lan_id==45:
        destination[0]='pf'
    if lan_id==46:
        destination[0]='pt'
    if lan_id==47:
        destination[0]='ro'
    if lan_id==48:
        destination[0]='ru'
    if lan_id==49:
        destination[0]='sr'
    if lan_id==50:
        destination[0]='sk'
    if lan_id==51:
        destination[0]='sl'
    if lan_id==52:
        destination[0]='es'
    if lan_id==53:
        destination[0]='sw'
    if lan_id==54:
        destination[0]='sv'
    if lan_id==55:
        destination[0]='ta'
    if lan_id==56:
        destination[0]='te'
    if lan_id==57:
        destination[0]='th'
    if lan_id==58:
        destination[0]='tr'
    if lan_id==59:
        destination[0]='uk'
    if lan_id==60:
        destination[0]='ur'
    if lan_id==61:
        destination[0]='vi'
    if lan_id==62:
        destination[0]='cy'
    if lan_id==63:
        destination[0]='yi'


    return redirect('/place/'+str(place_id))

def guide(request,guide_id):

    guide=get_object_or_404(Guide,pk=guide_id)
    return render(request,'guide/guide.html',{'guide':guide})

def ticket(request):
    tickets=Ticket.objects

    print(tickets)
    return render(request,'place/ticket.html',{'tickets':tickets})

def tick(request):
    ticket=Ticket(fname=request.POST['firstName'],lname=request.POST['lastName'],email=request.POST['email'],age=request.POST['age'],gender=request.POST['gr'],country=request.POST['country'],city=request.POST['city'],pincode=request.POST['pincode'],number='5522')

    ticket.save()
    return redirect('/ticket')
