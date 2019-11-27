import configparser
import json
import logging
import random

import jsonpath
import requests

logger = logging.getLogger('root')
logging.basicConfig(filename="/home/roman/GIT/git_Python/demo_pet/app/reports/pet_logger.log",
                    format='%(levelname)s %(asctime)s %(message)s ',
                    datefmt='%m/%d/%Y %I:%M:%S %p',
                    filemode='w',
                    level=logging.INFO)

config = configparser.RawConfigParser()
config.read('/home/roman/GIT/git_Python/demo_pet/sources/config.cfg')
base_url = config.get('demo-config-app', 'base_url')


class PetHelper():
    global test_body
    test_body = {}
    global headers
    headers = {'Content-Type': 'application/json'}

    def create_new_pet(self, reference_pet, st_code):
        body = json.loads(str(test_body).replace("\'", "\""))
        try:
            response = requests.post(base_url, json=body, headers=headers)
            status_code = response.status_code
            assert status_code == st_code, "STATUS CODE is not equal to " + str(
                status_code) + ". Reference status code is " + str(st_code)

        except Exception as err:
            logging.error(f'create_new_pet(): {err}')
        else:
            logging.info('Success!')
        # ****** collect common parameters by key ******
        try:
            pet_new_id = jsonpath.jsonpath(response.json(), 'id')
            new_pet_name = jsonpath.jsonpath(response.json(), 'name')
            new_pet_status = jsonpath.jsonpath(response.json(), 'status')
            new_category = jsonpath.jsonpath(response.json(), 'category.name')
            new_tagName = jsonpath.jsonpath(response.json(), 'tags[0].name')
            new_photoUrls = jsonpath.jsonpath(response.json(), 'photoUrls')
            pet_info_list = new_pet_name[0], new_category[0], new_pet_status[0], new_tagName[0], new_photoUrls[0][0]
            logging.info("reference_pet " + str(reference_pet))
            logging.info("'pet_info_list': " + str(pet_info_list))
        except ConnectionError as err:
            logging.error(f'create_new_pet(): - ConnectionError " {err}')
        except UnboundLocalError as err:
            logging.error(f'create_new_pet(): " {err}')
        return body, pet_info_list, pet_new_id, response

    def update_pet_name(self, pet_info_list, response_create, st_code, pet_new_name):
        logging.debug("response before_update: " + response_create.text)
        test_body['name'] = pet_new_name
        body = json.loads(str(test_body).replace("\'", "\""))
        name_before = pet_info_list.__getitem__(0)
        logging.debug("body after update " + str(body))
        try:
            response = requests.put(base_url, json=body, headers=headers)
            status_code = response.status_code
            assert status_code == st_code, "STATUS CODE is not equal to " + str(
                status_code) + ". Reference status code is " + str(st_code)
        except Exception as err:
            logging.error(f'update_pet_name(): {err}')
        else:
            logging.info('Success!')
        name_after = jsonpath.jsonpath(response.json(), 'name')
        logging.debug("name_before: " + str(name_before) + " | name_after: " + str(name_after[0]))
        assert name_before is not name_after

    def check_updated_pet(self, pet_new_id, st_code):
        new_url = str(base_url) + "/" + str(pet_new_id[0])
        try:
            response = requests.get(new_url, headers=headers)
            status_code = response.status_code
            assert status_code == st_code, "STATUS CODE is not equal to " + str(
                status_code) + ". Reference status code is " + str(st_code)
        except Exception as err:
            logging.error(f'check_updated_pet(): {err}')
        else:
            logging.info('Success!"Pet was checked!!!"')
        logging.info("GET response.text: " + response.text)
        return new_url

    def delete_pet(self, new_url, st_code):
        try:
            response = requests.delete(new_url, headers=headers)
            status_code = response.status_code
            assert status_code == st_code, "STATUS CODE is not equal to " + str(status_code)
        except Exception as err:
            logging.error(f'delete_pet(): {err}')
        else:
            logging.info('Success! "Pet deleted!!!"')

    def check_deleted_pet(self, new_url, st_code):
        try:
            response = requests.get(new_url, headers=headers)
            status_code = response.status_code
            logging.debug("DEL status_code: " + str(status_code))
            logging.debug("deleted_pet: st_code " + str(st_code) + " status_code " + str(status_code))
            assert status_code == st_code, "STATUS CODE is not equal to " + str(status_code)
        except Exception as err:
            logging.error(f'check_deleted_pet(): {err}')
        else:
            logging.info('Success! "Pet checked. It was deleted!!!" ')
        message = str(jsonpath.jsonpath(response.json(), 'message')[0])
        logging.info("Check deleted pet by ID- new_url : " + str(new_url))
        logging.info("Check deleted pet by ID- status code : " + str(status_code))
        logging.info("Check deleted pet by ID- error message : " + str(message))
        logging.info("Check deleted pet by ID: " + response.text)
        assert message == "Pet not found", "response_get_deleted- MESSAGE is invalid"

    def validate_id(self, body, pet_id, pet_new_id):
        assert pet_id == pet_new_id[0]
        logging.debug("pet_id: " + str(pet_id) + " | pet_new_id: " + str(pet_new_id[0]))
        logging.info("base BODY for 'create_new_pet()': " + str(body))

    def make_test_object(self, category_names, names, statuses, tagNames):
        try:
            # ****** generate test data for request body  ******
            pet_id = random.randint(1, 100)
            pet_second_id = random.randint(1, 10)
            pet_name = names[random.randint(0, len(names) - 1)]
            category_name = category_names[random.randint(0, len(category_names) - 1)]
            tagName = tagNames[random.randint(0, len(tagNames) - 1)]
            photoUrl = str("http://photoUrl/" + category_name + "/" + str(pet_id) + "/" + tagName)
            pet_tags = {"name": tagName, "id": pet_second_id}
            pet_status = statuses[random.randint(0, len(statuses) - 1)]
        except Exception as err:
            logging.error(f'make_test_object(), generating test data: {err}')
        # ****** create request body ******
        try:
            test_body["id"] = pet_id
            test_body["category"] = {'id': pet_second_id, 'name': category_name}
            test_body["name"] = pet_name
            test_body["photoUrls"] = [photoUrl]
            test_body["tags"] = [pet_tags]
            test_body["status"] = pet_status
            logging.info(test_body)
        except Exception as err:
            logging.error(f'make_test_object(), creating BODY error : {err}')
        return category_name, pet_id, pet_name, pet_status, photoUrl, tagName
