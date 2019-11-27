from app.app_helper import PetHelper


class TestApp():
    reference_pet = []
    category_names = ['DOG', 'CAT', 'FROG']
    names = ['Molly', 'Poppy', 'Alfie', 'Luna', 'Daisy']
    statuses = ['available', 'unavailable']
    tagNames = ['tag_one', 'tag_two']

    app = PetHelper()
    # ****** generate 'test_body' object parameters  ******
    category_name, pet_id, pet_name, pet_status, photoUrl, tagName = app.make_test_object(category_names, names,
                                                                                          statuses,
                                                                                          tagNames)
    reference_pet = pet_name, category_name, pet_status, tagName, photoUrl
    # create new PET"s by POST call
    body, pet_info_list, pet_new_id, response_create = app.create_new_pet(reference_pet, 200)
    # compare that initial id is the same as id from POST response body
    app.validate_id(body, pet_id, pet_new_id)
    # ****** update Pet_name by POST call ******
    app.update_pet_name(pet_info_list, response_create, 200, "newPETname")
    # ****** check updated pet by ID **********
    new_url = app.check_updated_pet(pet_new_id, 200)
    # ******** delete pet by ID ***********
    app.delete_pet(new_url, 200)
    # ******** check deleted pet by ID, status code should be 404, message: "Pet not found" ***********
    app.check_deleted_pet(new_url, 404)
