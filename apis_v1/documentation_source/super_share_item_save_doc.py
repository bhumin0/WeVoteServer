# apis_v1/documentation_source/super_share_item_save_doc.py
# Brought to you by We Vote. Be good.
# -*- coding: UTF-8 -*-


def super_share_item_save_doc_template_values(url_root):
    """
    Show documentation about superShareItemSave
    """
    required_query_parameter_list = [
        {
            'name':         'voter_device_id',
            'value':        'string',  # boolean, integer, long, string
            'description':  'An 88 character unique identifier linked to a voter record on the server',
        },
        {
            'name':         'api_key',
            'value':        'string (from post, cookie, or get (in that order))',  # boolean, integer, long, string
            'description':  'The unique key provided to any organization using the WeVoteServer APIs',
        },
        {
            'name':         'destination_full_url',
            'value':        'string',  # boolean, integer, long, string
            'description':  'The full URL with the final destination.',
        },
    ]
    optional_query_parameter_list = [
        {
            'name':         'ballot_item_we_vote_id',
            'value':        'string',  # boolean, integer, long, string
            'description':  'The we_vote_id for the ballot item being shared.',
        },
        {
            'name':         'google_civic_election_id',
            'value':        'integer',  # boolean, integer, long, string
            'description':  'The unique identifier for a particular election.',
        },
        {
            'name':         'is_ballot_share',
            'value':        'boolean',  # boolean, integer, long, string
            'description':  'The kind of destination shared: Ballot page',
        },
        {
            'name':         'is_candidate_share',
            'value':        'boolean',  # boolean, integer, long, string
            'description':  'The kind of destination shared: Candidate page',
        },
        {
            'name':         'is_measure_share',
            'value':        'boolean',  # boolean, integer, long, string
            'description':  'The kind of destination shared: Measure page',
        },
        {
            'name':         'is_office_share',
            'value':        'boolean',  # boolean, integer, long, string
            'description':  'The kind of destination shared: Office page',
        },
        {
            'name':         'is_organization_share',
            'value':        'boolean',  # boolean, integer, long, string
            'description':  'The kind of destination shared: Voter Guide page',
        },
        {
            'name':         'is_ready_share',
            'value':        'boolean',  # boolean, integer, long, string
            'description':  'The kind of destination shared: Ready page',
        },
    ]

    potential_status_codes_list = [
        {
            'code':         'VALID_VOTER_DEVICE_ID_MISSING',
            'description':  'Cannot proceed. A valid voter_device_id parameter was not included.',
        },
        {
            'code':         'VALID_VOTER_ID_MISSING',
            'description':  'Cannot proceed. A valid voter_id was not found.',
        },
    ]

    try_now_link_variables_dict = {
        # 'organization_we_vote_id': 'wv85org1',
    }

    api_response = '{\n' \
                   '  "status": string,\n' \
                   '  "success": boolean,\n' \
                   '  "destination_full_url": string,\n' \
                   '  "site_owner_organization_we_vote_id": string,\n' \
                   '  "shared_by_voter_we_vote_id": string,\n' \
                   '  "campaignx_we_vote_id": string,\n' \
                   '  "date_first_shared": datetime,\n' \
                   '}'

    template_values = {
        'api_name': 'superShareItemSave',
        'api_slug': 'superShareItemSave',
        'api_introduction':
            "",
        'try_now_link': 'apis_v1:superShareItemSaveView',
        'try_now_link_variables_dict': try_now_link_variables_dict,
        'url_root': url_root,
        'get_or_post': 'GET',
        'required_query_parameter_list': required_query_parameter_list,
        'optional_query_parameter_list': optional_query_parameter_list,
        'api_response': api_response,
        'api_response_notes':
            "",
        'potential_status_codes_list': potential_status_codes_list,
    }
    return template_values
