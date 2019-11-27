@pet_app
Feature:  As a tester, I want to check 'pet' API

  @create_new_pet
  Scenario: Creating 'pet' and validating status code
    Given I generate new pet object
    When I create new pet with status code 200

  @update_pet_name
  Scenario Outline: Updating pet_name after creating new one
    Given I generate new pet object
    When I create new pet with status code <status_code>
    Then I compare that pet_id is the same
    When I update pet name using <new_pet_name> with status code <status_code>
    Examples:
      | status_code | new_pet_name  |
      | 200         | first_update  |
      | 200         | second_update |

  @e2e
  Scenario Outline: End to end test for 'pet' API
    Given I generate new pet object
    When I create new pet with status code <valid_status_code>
    Then I compare that pet_id is the same
    When I update pet name using <new_pet_name> with status code <valid_status_code>
    Then I check updated pet by ID
    When I delete pet by ID with status code <valid_status_code>
    Then I check deleted pet by ID with status code <invalid_status_code>
    Examples:
      | valid_status_code | invalid_status_code | new_pet_name |
      | 200               | 200                 | first_update |






