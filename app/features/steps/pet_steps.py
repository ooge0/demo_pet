import sys

from behave import *

sys.path.append('/home/roman/GIT/git_Python/demo_pet')
from app.app_helper import PetHelper


class TestPet():
    # body = []
    # pet_id = 0
    # pet_new_id = 0

    @given(u'I generate new pet object')
    def generate_new_pet_object(self):
        # ****** generate 'test_body' object parameters  ******
        global reference_pet
        global pet_id
        category_names = ['DOG', 'CAT', 'FROG']
        names = ['Molly', 'Poppy', 'Alfie', 'Luna', 'Daisy']
        statuses = ['available', 'unavailable']
        tagNames = ['tag_one', 'tag_two']
        app = PetHelper()
        category_name, pet_id, pet_name, pet_status, photoUrl, tagName = app.make_test_object(category_names, names,
                                                                                              statuses, tagNames)
        reference_pet = pet_name, category_name, pet_status, tagName, photoUrl
        print(reference_pet)

    @when(u'I create new pet with status code {st_code}')
    def create_new_pet(self, st_code):
        ## ******  create new PET"s by POST call  ******
        global body
        global pet_new_id
        global pet_info_list
        global response_create
        app = PetHelper()
        body, pet_info_list, pet_new_id, response_create = app.create_new_pet(reference_pet, st_code)

    @then(u'I compare that pet_id is the same')
    def compare_pet_id(self):
        # compare that initial id is the same as id from POST response body
        app = PetHelper()
        app.validate_id(body, pet_id, pet_new_id)

    @when(u'I update pet name using {new_pet_name} with status code {st_code}')
    def update_pet_name(self, new_pet_name, st_code):
        # ****** update Pet_name by POST call ******
        global update_pet_name_st_code
        update_pet_name_st_code = st_code
        app = PetHelper()
        app.update_pet_name(pet_info_list, response_create, st_code, new_pet_name)

    @then(u'I check updated pet by ID')
    def compare_pet_id(self):
        global new_url
        # ****** check updated pet by ID **********
        app = PetHelper()
        new_url = app.check_updated_pet(pet_new_id, update_pet_name_st_code)

    @when(u'I delete pet by ID with status code {st_code}')
    def delete_pet_by_id(self, st_code):
        # ******** delete pet by ID ***********
        app = PetHelper()
        app.delete_pet(new_url, st_code)

    @then(u'I check deleted pet by ID with status code {st_code}')
    def check_deleted_pet_by_ID(context, st_code):
        # # ******** check deleted pet by ID, status code should be 404, message: "Pet not found" ***********
        app = PetHelper()
        app.check_deleted_pet(new_url, st_code)

