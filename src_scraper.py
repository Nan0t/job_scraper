from datetime import date
import pprint
import requests
from bs4 import BeautifulSoup

today = date.today().strftime("%d/%m/%Y")
def busquedaEmpleosIT(nombrePuesto):
    listaEmpleos=[]
    puestoFormateado= nombrePuesto.replace(' ','+')
    URL='https://www.empleosit.com.ar/search-results-jobs/?action=search&listing_type%5Bequal%5D=Job&keywords%5Ball_words%5D={puestoArg}&Location%5Blocation%5D%5Bvalue%5D=Ciudad+Autónoma+de+Buenos+Aires%2C+Buenos+Aires&Location%5Blocation%5D%5Bradius%5D=10&listings_per_page=20'.format(puestoArg= puestoFormateado)
    page = requests.get(URL)
    soup = BeautifulSoup(page.content, 'html.parser')
    results = soup.find(id='listingsResults')
    jobsWithListingRight= results.find_all(class_='listing-right')

    for jobWithListingRight in jobsWithListingRight:
        jobWithListingTitle=jobWithListingRight.find(class_='listing-title')
        date= jobWithListingRight.find(class_='captions-field posted-ico').get_text()
        if (date == today):
            anchorElements=jobWithListingTitle.find_all('a')
            for anchorElement in anchorElements:
                link=anchorElement.get('href')
                if(link is not None):
                    listaEmpleos.append(link)

    return listaEmpleos



def busquedaEnEducacionIT(nombrePuesto):
    listaEmpleos=[]
    dominioPagina="https://www.educacionit.com/"
    puestoFormateado= nombrePuesto.replace(' ','+')
    URL='https://www.educacionit.com/empleos.php?busqueda_laboral=&bus_texto={puestoArg}&busqueda_puesto2=&bus_provincia=174'.format(puestoArg= puestoFormateado)
    page= requests.get(URL)
    soup = BeautifulSoup(page.content, 'html.parser')
    jobDivs=soup.find_all(class_='itemEmpleo posr')

    for div in jobDivs:
        date= div.find(class_='fechaEmpleo').get_text()
        if (date == today):
            ultimaParteLink=div.find(class_= 'fwN').get('href')
            empleoURL=dominioPagina + ultimaParteLink
            listaEmpleos.append(empleoURL)

    return listaEmpleos



def buscarEmpleos(empleosBuscadosArg):
    listaLinks=[]
    for empleoBuscado in empleosBuscadosArg:
        listaLinks.extend(busquedaEmpleosIT(empleoBuscado))
        listaLinks.extend(busquedaEnEducacionIT(empleoBuscado))
    return listaLinks
