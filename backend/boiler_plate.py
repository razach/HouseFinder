url = "https://www.realtor.com/api/v1/hulk_main_srp"

apistring = {"client_id": "rdc-x", "schema": "vesta"}

headers = {
"authority": "www.realtor.com",
"accept": "application/json",
"accept-language": "en-US,en;q=0.5",
"content-type": "application/json",
"origin": "https://www.realtor.com",
"sec-fetch-dest": "empty",
"sec-fetch-mode": "cors",
"sec-fetch-site": "same-origin",
"sec-gpc": "1",
"user-agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36"
}


for_sale_query = """
    query ConsumerSearchMainQuery(
        $query: HomeSearchCriteria!
        $limit: Int
        $offset: Int
        $sort: [SearchAPISort]
        $sort_type: SearchSortType
        $client_data: JSON
        $bucket: SearchAPIBucket
        ) {
        home_search: home_search(
            query: $query
            sort: $sort
            limit: $limit
            offset: $offset
            sort_type: $sort_type
            client_data: $client_data
            bucket: $bucket
        ) {
            count
            total
            results {
            property_id
            list_price
            primary
            rent_to_own {
                rent
                right_to_purchase
                provider
            }
            primary_photo(https: true) {
                href
            }
            source {
                id
                agents {
                office_name
                }
                type
                spec_id
                plan_id
            }
            community {
                property_id
                permalink
                description {
                name
                }
                advertisers {
                office {
                    hours
                    phones {
                    type
                    number
                    }
                }
                builder {
                    fulfillment_id
                }
                }
            }
            products {
                brand_name
                products
            }
            listing_id
            matterport
            virtual_tours {
                href
                type
            }
            status
            permalink
            price_reduced_amount
            other_listings {
                rdc {
                listing_id
                status
                listing_key
                primary
                }
            }
            description {
                beds
                baths
                baths_full
                baths_half
                baths_1qtr
                baths_3qtr
                garage
                stories
                type
                sub_type
                lot_sqft
                sqft
                year_built
                sold_price
                sold_date
                name
            }
            location {
                street_view_url
                address {
                line
                postal_code
                state
                state_code
                city
                coordinate {
                    lat
                    lon
                }
                }
                county {
                name
                fips_code
                }
            }
            tax_record {
                public_record_id
            }
            lead_attributes {
                show_contact_an_agent
                opcity_lead_attributes {
                cashback_enabled
                flip_the_market_enabled
                }
                lead_type
                ready_connect_mortgage {
                show_contact_a_lender
                show_veterans_united
                }
            }
            open_houses {
                start_date
                end_date
                description
                methods
                time_zone
                dst
            }
            flags {
                is_coming_soon
                is_pending
                is_foreclosure
                is_contingent
                is_new_construction
                is_new_listing(days: 14)
                is_price_reduced(days: 30)
                is_plan
                is_subdivision
            }
            list_date
            last_update_date
            coming_soon_date
            photos(limit: 2, https: true) {
                href
            }
            tags
            branding {
                type
                photo
                name
            }
            }
        }
    }
"""

for_rent_query = """
    query ConsumerSearchMainQuery(
        $query: HomeSearchCriteria!
        $limit: Int
        $offset: Int
        $sort: [SearchAPISort]
        $sort_type: SearchSortType
        $client_data: JSON
        $bucket: SearchAPIBucket
        ) {
        home_search: home_search(
            query: $query
            sort: $sort
            limit: $limit
            offset: $offset
            sort_type: $sort_type
            client_data: $client_data
            bucket: $bucket
        ) {
            count
            total
            results {
            property_id
            list_price
            primary
            rent_to_own {
                rent
                right_to_purchase
                provider
            }
            primary_photo(https: true) {
                href
            }
            source {
                id
                agents {
                office_name
                }
                type
                spec_id
                plan_id
            }
            community {
                property_id
                permalink
                description {
                name
                }
                advertisers {
                office {
                    hours
                    phones {
                    type
                    number
                    }
                }
                builder {
                    fulfillment_id
                }
                }
            }
            products {
                brand_name
                products
            }
            listing_id
            matterport
            virtual_tours {
                href
                type
            }
            status
            permalink
            price_reduced_amount
            other_listings {
                rdc {
                listing_id
                status
                listing_key
                primary
                }
            }
            description {
                beds
                baths
                baths_full
                baths_half
                baths_1qtr
                baths_3qtr
                garage
                stories
                type
                sub_type
                lot_sqft
                sqft
                year_built
                sold_price
                sold_date
                name
            }
            location {
                street_view_url
                address {
                line
                postal_code
                state
                state_code
                city
                coordinate {
                    lat
                    lon
                }
                }
                county {
                name
                fips_code
                }
            }
            tax_record {
                public_record_id
            }
            lead_attributes {
                show_contact_an_agent
                opcity_lead_attributes {
                cashback_enabled
                flip_the_market_enabled
                }
                lead_type
                ready_connect_mortgage {
                show_contact_a_lender
                show_veterans_united
                }
            }
            open_houses {
                start_date
                end_date
                description
                methods
                time_zone
                dst
            }
            flags {
                is_coming_soon
                is_pending
                is_foreclosure
                is_contingent
                is_new_construction
                is_new_listing(days: 14)
                is_price_reduced(days: 30)
                is_plan
                is_subdivision
            }
            list_date
            last_update_date
            coming_soon_date
            photos(limit: 2, https: true) {
                href
            }
            tags
            branding {
                type
                photo
                name
            }
            }
        }
    }
"""

school_url = "https://www.realtor.com/api/v1/hulk"

school_header = {
            "authority": "www.realtor.com",
            "accept": "*/*",
            "accept-language": "en-US,en;q=0.9",
            "sec-fetch-dest": "empty",
            "sec-fetch-mode": "cors",
            "sec-fetch-site": "same-origin",
            "sec-gpc": "1",
            "user-agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36"
        }

school_query = """
    query GetLocalData($propertyId: ID!) {
        home(property_id: $propertyId) {
            schools {
                total
                    schools {
                    id
                    name
                    slug_id
                    education_levels
                    distance_in_miles
                    student_teacher_ratio
                    rating
                    grades
                    funding_type
                    student_count
                    review_count
                    parent_rating
                    assigned
                }
            }
        }
    }
    """
        
