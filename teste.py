from asyncio.log import logger
import requests
import sys
from tqdm import tqdm
from concurrent.futures import ThreadPoolExecutor
import os

def download_files():
    """
    Downloads files from the internet using links provided in a text file and saves them in a download directory.
    Returns
    -------
    None
    """
    file = open('input.txt', 'r')
    Lines = file.readlines()

    list_of_links = []
    for line in Lines:
        list_of_links.append(line.strip())


    def get_files(link):
        """
        Downloads files from a link.

        Parameters
        ----------
        link: str
            string with link to download from

        Raises
        -----
        HTTPError
            404 Client Error: Not Found for url:
        
        Returns
        -------
        None
        """
        
        
        
        
        name = link.split('/')
        name = sys.argv[1] + "/" + name[-1]
        try:
            response = requests.get(link)
            response.raise_for_status()
            print(link)
            try:
                with tqdm.wrapattr(open(name, 'wb'), "write",miniters=1,
                total=int(response.headers.get('content-length', 0))) as output_img:
                    for chunk in response.iter_content(chunk_size=4096):
                        output_img.write(chunk)
                return "{result} {address} OK".format(result=response.status_code, address=link)        
            except Exception as e:
                print(e.__str__)
                pass
        except requests.exceptions.HTTPError as err:
            return str(err)
    with ThreadPoolExecutor(max_workers=4) as pool:
        response_list = list(pool.map(get_files, list_of_links))
    for response in response_list:
        print(response)
    
    return None
    
      

        
try:
    if __name__ == '__main__':
        try:
            sys.argv[1]
            filepath = os.path.exists(sys.argv[1])
            if filepath == False:
                print("Directory provided to save files does not exist")
                sys.exit(1)
        except IndexError:
            print("You did not specify a file")
            sys.exit(1)

        download_files()
except KeyboardInterrupt:
    print("KeyboardInterrupt")
    exit(0)





