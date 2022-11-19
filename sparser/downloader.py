from pprint import pprint
from turtle import down
import requests
import json
import os
import time

from HtmlSparser import HtmlSparser

'''
['292160', '624937', '501550', '540917', '437728', '339680', '460495', '536489', '538925', '547431', '551438', '413847', '236863', '544480', '617356', '574427', '389911', '339675', '21529', '624938', '625374', '483829', '614126', '559836', '559350', '590612', '623491', '623490', '483821', '623488', '623597', '558296', '524264', '622671', '622283', '623041', '552000', '623038', '491926', '597393', 
'621519', '596843', '451077', '621002', '554499', '624018', '549131', '424285', '623812', '602852', '623813', '354240', '429148', '579349', '347565', '579325', '577194', '506486', '559258', '520707', '485623', '388848', '608679', '438069', '623485', '217854', '616057', '564835', '304858', '353444', '623335', '556063', '623475', '423113', '498188', '456524', '625633', '603554', '606583', '604199', '610236', '585665', '612968', '256662', '571764', '603068', '608450', '590490', '364023', '586570', '486305', '569728', '603644', '622982', '597507', '192421', '622591', '504670', '592807', '619664', '620393', '605461', '625644', '587065', '611082', '584315', '613060', '615748', '623481', '151618', '527071', '558737', '620178', '193692', '593323', '625320', '610233', '451083', '494504', '553216', '624862', '450718', '376292', '584408', '558790', '432099', '350922', '583280', '494759', '613088', '277642', '612965', '240623', '622964', '623337', '625634', '613044', '625170', '622118', '625300', '625465', '601191', '583242', 
'619641', '622005', '262153', '308292', '283515', '615120', '573409', '282643', '315317', '393549', '82636', '412368', '577060', '622197', '192412', '624804', '610766', '615818', '138349', '622720', '597492', '584341', '530603', '621893', '191251', '618882', '603502', '552760', '589150', '623623', '307165', '584317', '619655', '625639', '589272', '169296', '527124', '461422', '478827', '511815', '446152', '619625', '621082', '623863', '612990', '613478', '616797', '592139', '624883', '620392', '617402', '622729', '543147', '620397', '11652', '621071', '478234', '528590', '619650', '612246', '617972', '624814', 
'527158', '621730', '415352', '621334', '466357', '608937', '620470', '625204', '294349', '58733', '614152', '460430', '599210', '446795', '608981', '593807', '618299', '587114', '612979', '622274', '259909', '523795', '390998', '555920', '501941', '239778', '621752', '585845', '622448', '603686', '623074', '623627', '625366', '543145', '151623', '623681', '622955', '589679', '614157', '624050', '455457', '612534', '619194', '622736', '499330', '573402', '574828', '546542', '622956', '521560', '558154', '613082', '619629', '623244', '275171', '623581', '23293', '619594', '519386', '584916', '624223', '506809', 
'621732', '417951', '610471', '623673', '586360', '260137', '603506', '622718', '536833', '304679', '620471', '570891', '584296', '363704', '419055', '172445', '625308', '549842', '595783', '415349', '613020', '624579', '621049', '603503', '623638', '603979', '277633', '535044', '615398', '568186', '600995', '623002', '550446', '565183', '595782', '552764', '619623', '625529', '485222', '325643', '543146', '496045', '625198', '590460', '622001', '596975', '466898', '317627', '607659', '624855', '613074', '475330', '532046', '620861', '590453', '610765', '613035', '353932', '531587', '585887', '619668', '623837', '595376', '623075', '491084', '620177', '295066', '621691', '566940', '622737', '596825', '623199', '584398', '621332', '446381', '562912', '583708', '607246', '578582', '619639', '51242', '287261', '584405', '275169', '620458', '595790', '574831', '335760', '624895', '622872', '623374', '615744', '48790', '41856', '624516', '597770', '623921', '623215', '598591', '548484', '442247', '622470', '624609', '496043', '527123', '613014', '368611', '595789', '469038', '593334', '597418', '622723', '604958', '505897', '625637', '611352', '597254', '622182', '624427', '613479', '622660', '508495', '605912', '620922', '585666', '622399', '558617', '591008', '4577', '603984', '586571', '614158', '495199', '536832', '623070', '562002', '488984', '621746', '401569', '622610', '390749', '583871', '564358', '618939', '191254', '570224', '494090', '619620', '419067', '588228', '496210', '622285', '451306', '417835', '440540', '621897', '616551', '621210', '530072', '593332', '560531', '623333', '600769', '618283', '577496', '501928', '613066', '465291', '623078', '50263', '450690', '510037', '595788', '235780', '616772', '597491', '302357', '504301', '623338', '622004', '460983', '615593', '622721', '601179', '313646', '527166', 
'441287', '499337', '617933', '625725', '592806', '579312', '595593', '610744', '619360', '559748', '511531', '352845', '620141', '595794', '436013', '327753', '496049', '563318', '621323', '614889', '622734', '528032', '597424', '590454', '620139', '615759', '573408', '611815', '620014', '623704', '619015', '623663', '612296', '584338', '607337', '622971', '619678', '622284', '591757', '624612', '465607', '556599', '446791', '621053', '573407', '334235', '614159', '624587', '500515', '535620', '617859', '622650', '451081', '316287', '622584', '550443', '613076', '585667', '411603', '512194', '464447', '624056', '11730', '556062', '622627', '581836', '60910', '554341', '570220', '364020', '536099', '609465', '621056', '621057', '625464', '622916', '597225', '618721', '612382', '624903', '591044', '583826', '597419', '622588', '584672', '622500', '586580', '509850', '346309', '606739', '623577', '624599', '613006', '625321', '625638', '613051', '417408', '603687', '574380', '534590', '539280', '550457', '615113', '519117', '470058', '612958', '304714', '621047', '137385', '273402', '613012', '614290', '605958', '518164', '483448', '622580', '334851', '614948', '619118', '622876', '594316', '597493', '547605', '601531', '474599', '623661', '442033', '373524', '622408', '307168', '449652', '597276', '613003', '454418', '619019', '516971', '517535', '625301', '491541', '612966', '578580', '625466', '556495', '610472', '613053', '584313', '613934', '615021', '624576', '623873', '622578', '607251', '625470', '625722', '623715', '552200', '604548', '619507', '622376', '553746', '221621', '617858', '556007', '479428', '603047', 
'393544', '623679', '313196', '466899', '622722', '621744', '595780', '582325', '565077', '585531', '620474', '572393', '623665', '311817', '520535', '586900', '547602', '559867', '527221', '537289', '495687', '615408', '532525', '230809', '621979', '575595', '576385', '611353', '607575', '325642', '489756', '565920', '612974', '579408', '621690', '597988', '604549', '622579', '615360', '587473', '615808', '603685', '603928', '307167', '417948', '592336', '625085', '478066', '614151', '350914', '593117', '617190', '620398', '625357', '440871', '511530', '591816', '75464', '621213', '612976', '615016', '536831', '546555', '546637', '623336', '499335', '622958', '612383', '547603', '625353', '613041', '596868', '607247', '558170', '391303', '586573', '621157', '466895', '613004', '619630', '622959', '613045', '294354', '540550', '521456', '166740', '567602', '558618', '621211', '622119', '574827', '622719', '48209', '555756', '617971', '583709', '526859', '616773', '533455', '593218', '598854', '620140', '515566', '618206', '621425', '624580', '590698', '624221', '609356', '612964', '384824', '617965', '613027', '516953', '481064', '557107', '618933', '20896', '622395', '338583', '80982', '619355', '496048', '616532', 
'621329', '475832', '613619', '616056', '191250', '601134', '625345', '592795', '622328', '496047', '603675', '625471', '624572', '622735', '511528', '552768', '621004', '514067', '612971', '592258', '573404', '282418', '295371', '573403', '577926', '622369', '616553', '624616', '512918', '625447', '527152', '625304', '501193', '384221', '620210', '563188', '592243', '582971', '599255', '388657', '616776', '477252', '616054', '618277', '571804', '620472', '623322', '494501', '624888', '621333', '621050', '442063', '594283', '613015', '610628', '86473', '619632', '622294', '615753', '584340', '516952', '623184', '519087', '602372', '622577', '55251', '613016', '625222', '577193', '622989', '235482', '421725', '579707', '625291', '612970', '307176', '598693', '576145', '620399', '625207', '570221', '602455', '576933', '544105', '277634', '550928', '480137', '600709', '363711', '622878', '615765', '624605', '610852', '622873', '611585', '444306', '471767', '622654', '605627', '615755', '622183', '601511', '612384', '452724', '492771', '543144', '622651']
'''

'''
masterValues key histogram:
 'actual-price': 9,
 'alcohol-level-filter': 1248,
 'allergens-filter': 12160,
 'approx-weight-product': 17756,
 'badge-icon': 6576,
 'badge-names': 6576,
 'badge-short-name': 6576,
 'best-price': 17756,
 'categories': 17536,
 'category-id': 17756,
 'category-name': 17341,
 'category-names': 17536,
 'category-path': 17536,
 'code-internal': 17756,
 'created-at': 17756,
 'description': 17756,
 'ecr-brand': 17723,
 'ecr-category-number': 17756,
 'egg-size-filter': 53,
 'energy-class-filter': 54,
 'farming-method-filter': 58,
 'fat-content-filter': 233,
 'for-ages-filter': 3,
 'image-url': 17756,
 'is-new': 17756,
 'is-on-promotion': 17756,
 'item-type': 17756,
 'life-expectancy-filter': 54,
 'name': 17756,
 'pos-purchasable': 17749,
 'pos-visible': 17756,
 'power-filter': 76,
 'price': 17756,
 'price-per-unit': 17756,
 'price-per-unit-number': 17756,
 'product-features': 4286,
 'product-number': 17756,
 'promotion-most-likely-text': 379,
 'promotion-text': 2733,
 'quantity-selector': 407,
 'regular-price': 17756,
 'sales-unit': 17756,
 'screw-type-filter': 54,
 'short-description': 7332,
 'short-description-2': 7332,
 'stock-status': 17756,
 'taste-filter': 630,
 'title': 17756,
 'url': 17756,
 'wine-area-filter': 466

variantValues histogram:
  [] all



'''


class SparDownloader:
    def __init__(self, search_json):
        self.data = search_json['hits']

        if 'item_html' in search_json.keys():
            self.item_html = search_json['item_html']
        else:
            self.item_html = {}

    @classmethod
    def from_get_request(cls, hits_per_page=100000):
        return cls(requests.get(
            f"https://search-spar.spar-ics.com/fact-finder/rest/v4/search/products_lmos_si?query=*&page=1&hitsPerPage={hits_per_page}"
        ).json())
    

    def save_data(self, filename="search-spar.json", include_html=False):
        with open(filename, "w", encoding="utf8") as f:
            out = {
                "hits":self.data
            }
            if(include_html):
                out['item_html'] = self.item_html

            f.write(json.dumps(out))
    
    def save_data_to_files(self, overwrite=False, folder="products"):
        if not os.path.exists(folder):
            print("making folder")
            os.mkdir(folder)
            print("done")
        
        for key in self.item_html:
            path = f"{folder}/{key}.html"
            if overwrite or not os.path.exists(path):
                with open(path, "w", encoding="utf8") as file:
                    file.write(self.item_html[key])
    
    @classmethod
    def from_initial_json(cls, filename="search-spar.json"):
        with open(filename, encoding="utf8") as f:
            return cls(json.loads(f.read()))

    @classmethod
    def from_initial_files(cls, folder="products", filename="search-spar.json"):
        instance = cls.from_initial_json(filename)

        i = 0
        files = [f"{f['id']}.html" for f in instance.data]
        for filename in files:
            if os.path.exists(f"{folder}/{filename}"):
                with open(f"{folder}/{filename}", "r", encoding="utf8") as file:
                    instance.item_html[filename.split(".")[0]] = file.read()
            
                print(f"loaded {i+1}/{len(files)}")
            i += 1
        
        return instance
    
    def download_from_hits(self, disable_cached=False, filename="data.json", folder="products", save_as_files=True):
        if self.data == None or len(self.data) == 0:
            raise "no initial request data loaded"
        
        if self.item_html == None:
            self.item_html = {}
        
        print(self.item_html.keys())
        i = 0

        unsaved_requests = 0
        
        for item in self.data:
            status = ""

            if not disable_cached and item['id'] in self.item_html.keys() or save_as_files and not disable_cached and os.path.exists(f"{folder}/{item['id']}.html"):
                status = "/"
            else:
                try:
                    html = requests.get(
                        f"https://www.spar.si/online{item['masterValues']['url']}"
                    ).text

                    self.item_html[item['id']] = html

                    if unsaved_requests > 300:
                        print(f"saving data... ({len(self.item_html)} files)")
                        start = time.time()
                        if save_as_files:
                            self.save_data_to_files()
                            self.item_html = {}
                        else:
                            self.save_data(filename)
                        print(f"done in {(time.time() - start):.2f} seconds")

                        unsaved_requests = 0

                    unsaved_requests += 1

                    status="O"
                except Exception as e:
                    print("Exception:", e)
                    status="X"
            
            url = "https://www.spar.si/online"+ item['masterValues']['url'] if status=="O" else ""
            print(f"<{i:5d}/{unsaved_requests:3d}/{len(self.data)}>[{status}] {item['masterValues']['title']} {url}")
            if status != "/":
                time.sleep(.5)

            i+=1

    # Helpers
    def valueSet(self, key):
        out = []
        for i in self.data:
            if key in i['masterValues']:
                if isinstance(i['masterValues'][key], list):
                    for k in i['masterValues'][key]:
                        if k not in out:
                            out.append(k)
                else:
                    if i['masterValues'][key] not in out:
                        out.append(i['masterValues'][key])
        return out
    
    def keySet(self):
        out = {}
        for i in self.data:
            for key in i['variantValues'].keys():
                if key in out.keys():
                    out[key] += 1
                else:
                    out[key] = 1
        return out

    def __str__(self):
        return f'<SparDownloader obj>\n{len(self.data)} hits from initial request\n{len(self.item_html.keys())} loaded item htmls'

if __name__ == "__main__":
    '''
    # download all loop
    try:
        downloader_obj = SparDownloader.from_initial_json("search-spar.json")

        print(str(downloader_obj))

        downloader_obj.download_from_hits()

        print("saving data...")
        start = time.time()
        downloader_obj.save_data_to_files("data.json")
        print(f"done in {(time.time() - start):.2f} seconds")
    except KeyboardInterrupt:
        print("saving data...")
        start = time.time()
        downloader_obj.save_data_to_files("data.json")
        print(f"done in {(time.time() - start):.2f} seconds")
        exit(0)
    '''
    downloader_obj = SparDownloader.from_initial_files()

    files_not_found = []

    for i, product in enumerate(downloader_obj.data):
        if product['id'] in downloader_obj.item_html.keys():
            parsed = HtmlSparser(downloader_obj.item_html[product['id']]).parse().item_data
            product['parsed-data'] = {}

            for key in parsed.keys():
                product['parsed-data'][key] = parsed[key]
        
            print(f"Parsed {i+1}/{len(downloader_obj.data)}")
        else:
            files_not_found.append(product['id'])
            print(f"File not found {product['id']}")

    print("not found: ", files_not_found)
    
    print("saving...")
    print("saving data...")
    start = time.time()
    downloader_obj.save_data_to_files("data.json")
    print(f"done in {(time.time() - start):.2f} seconds")

