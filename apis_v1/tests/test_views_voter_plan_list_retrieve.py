# apis_v1/test_views_voter_plan_list_retrieve.py
# Brought to you by We Vote. Be good.
# -*- coding: UTF-8 -*-

import json
from django.test import Client, TestCase
from voter.models import VoterPlan

#file path: /workspaces/WeVoteServer/apis_v1/tests/test_views_voter_plan_list_retrieve

# unit tests for voter plan list 
# 1. trying an invalid election id: should return an error response. 
# 2. testing number of voter plans: Creating two plan voter plan objects with the same id, What will be returned
# 3. checking if the voter plan retrieve provides the expected keys/data types.

class WeVoteAPIsV1TestsVoterPlanListRetrieve(TestCase):
    databases = ["default", "readonly"]

    def setUp(self):
        self.client = Client()

        # Creating a voter
        self.voter_plan = VoterPlan.objects.create(
            google_civic_election_id=1234,
            state_code="CA",
            voter_display_name="Joe Doe",
            voter_display_city_state="San Francisco, CA",
            voter_we_vote_id="ABCDEF",
            voter_plan_data_serialized="{}",
            voter_plan_text="Hi",
            show_to_public=True,
        )


    # Testing to see if multiple voters will pop up with the same civic election id
    def test_number_of_voter_plans(self):
        VoterPlan.objects.create(
            google_civic_election_id=1234,
            state_code="HI",
            voter_display_name="Jae Doe",
            voter_display_city_state="Los Angeles, CA",
            voter_we_vote_id="UVWXYZ",
            voter_plan_data_serialized="{}",
            voter_plan_text="Hi",
            show_to_public=True,
        )
        response = self.client.get('/voter_plan_list_retrieve/', {'google_civic_election_id': 1234})
        json_response = json.loads(response.content)
        self.assertEqual(len(json_response['voter_plan_list']), 2)
        
    # Checking to see if the google civic election id is invalid
    def test_invalid_google_civic_election_id(self):
        response = self.client.get('/voter_plan_list_retrieve/', {'google_civic_election_id': 'invalid'})
        self.assertEqual(response.status_code, 200)
        json_response = json.loads(response.content)
        self.assertFalse(json_response['success'])
        self.assertIn('status', json_response)
        self.assertIn('RETRIEVE_VOTER_PLAN_LIST_FAILED', json_response['status'])

    def test_voter_plan_list_retrieve_view(self):
        # Send a request with the google_civic_election_id parameter
        response = self.client.get('/voter_plan_list_retrieve/', {'google_civic_election_id': 1234})

        # Check that the response has a status code of 200
        self.assertEqual(response.status_code, 200)

        # Check that the JSON response has the expected keys and data types
        expected_keys = {'success', 'status', 'voter_plan_list'}
        self.assertSetEqual(set(response.json().keys()), expected_keys)
        self.assertIsInstance(response.json()['success'], bool)
        self.assertIsInstance(response.json()['status'], str)
        self.assertIsInstance(response.json()['voter_plan_list'], list)

        # Check that the voter_plan_list has the expected keys and data types
        if len(response.json()['voter_plan_list']) > 0:
            voter_plan = response.json()['voter_plan_list'][0]
            expected_voter_plan_keys = {
                'google_civic_election_id', 
                'state_code', 
                'voter_display_name',
                'voter_display_city_state', 
                'voter_we_vote_id', 
                'voter_plan_data_serialized',
                'voter_plan_text', 
                'show_to_public', 
                'date_entered', 
                'date_last_changed',
                'we_vote_hosted_profile_image_url_medium'}

            self.assertSetEqual(set(voter_plan.keys()), expected_voter_plan_keys)
            self.assertIsInstance(voter_plan['google_civic_election_id'], int)
            self.assertIsInstance(voter_plan['state_code'], str)
            self.assertIsInstance(voter_plan['voter_display_name'], str)
            self.assertIsInstance(voter_plan['voter_display_city_state'], str)
            self.assertIsInstance(voter_plan['voter_we_vote_id'], str)
            self.assertIsInstance(voter_plan['voter_plan_data_serialized'], str)
            self.assertIsInstance(voter_plan['voter_plan_text'], str)
            self.assertIsInstance(voter_plan['show_to_public'], bool)
            self.assertIsInstance(voter_plan['date_entered'], str)
            self.assertIsInstance(voter_plan['date_last_changed'], str)
            self.assertIsInstance(voter_plan['we_vote_hosted_profile_image_url_medium'], str)