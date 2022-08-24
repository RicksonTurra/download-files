import requests
import sys
from tqdm import tqdm

def download_files():
    """
    Downloads files from the internet using links provided in a text file and saves them in a download directory.
    Returns
    -------
    Function call: get_files(list_of_links)
    """
    file = open('input.txt', 'r')
    Lines = file.readlines()

    list_of_links = []
    for line in Lines:
        list_of_links.append(line.strip())

    def get_files(links):
        """
        Downloads files from a list of links.

        Parameters
        ----------
        links: List[str]
            list of links to have data downloaded from

        Raises
        -----
        HTTPError
            404 Client Error: Not Found for url:
        
        Returns
        -------
        None
        """

        for each in list_of_links:
            name = each.split('/')
            name = sys.argv[1] + "/" + name[-1]
            try:
                response = requests.get(each)
                response.raise_for_status
                with tqdm.wrapattr(open(name, 'wb'), "write",miniters=1,
                total=int(response.headers.get('content-length', 0))) as output_img:
                    for chunk in response.iter_content(chunk_size=4096):
                        output_img.write(chunk)
            except requests.exceptions.HTTPError as err:
                raise SystemExit(err)
    return get_files(list_of_links)

        
try:
    if __name__ == '__main__':
        download_files()
except KeyboardInterrupt:
    print("GOOODBYEEEEEE")
    exit(0)





