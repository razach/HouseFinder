Boundary = {
			"type": "Polygon",
			"coordinates": [
				[
					[
						-77.44898,
						38.86813
					],
					[
						-77.44,
						38.85764
					],
					[
						-77.41416,
						38.84014
					],
					[
						-77.37822,
						38.83139
					],
					[
						-77.35351,
						38.82002
					],
					[
						-77.31981,
						38.78238
					],
					[
						-77.27264,
						38.7491
					],
					[
						-77.24119,
						38.7342
					],
					[
						-77.19851,
						38.71931
					],
					[
						-77.1884,
						38.72194
					],
					[
						-77.18503,
						38.72719
					],
					[
						-77.1693,
						38.785
					],
					[
						-77.15583,
						38.80076
					],
					[
						-77.11764,
						38.80339
					],
					[
						-77.08731,
						38.79901
					],
					[
						-77.080164,
						38.79641029792285
					],
					[
						-77.080164,
						38.905333636363636
					],
					[
						-77.08169,
						38.90573
					],
					[
						-77.10079,
						38.91534
					],
					[
						-77.11178650548938,
						38.92637
					],
					[
						-77.42490248618785,
						38.92637
					],
					[
						-77.42539,
						38.91534
					],
					[
						-77.44898,
						38.87425
					],
					[
						-77.44898,
						38.86813
					]
				]
			]
		}

user_param_for_sale = {
    "status": ["for_sale", "ready_to_build"],
    "primary": True,
    "type": ["single_family"],
	"list_price": {"max": 700000},
    # "search_location": {"location": "Burke, VA"}
    "boundary": Boundary
}

user_param_for_rent = {
    "status": ["for_rent"],
    "primary": True,
    "type": ["single_family"],
    # "search_location": {"location": "Burke, VA"}
    "boundary": Boundary
}