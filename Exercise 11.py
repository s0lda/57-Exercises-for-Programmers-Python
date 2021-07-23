import requests

# hardcoded currency codes as my free API key allows only a few requests
codes = {
'AED': 'United Arab Emirates',
'AFN': 'Afghanistan',
'ALL': 'Albania',
'AMD': 'Armenia',
'ANG': 'Netherlands',
'AOA': 'Angola',
'ARS': 'Argentina',
'AUD': 'Australia',
'AWG': 'Aruba',
'AZN': 'Azerbaijan',
'BAM': 'Bosnia and Herzegovina',
'BBD': 'Barbados',
'BDT': 'Bangladesh',
'BGN': 'Bulgaria',
'BHD': 'Bahrain',
'BIF': 'Burundi',
'BMD': 'Bermuda',
'BND': 'Brunei',
'BOB': 'Bolivia',
'BRL': 'Brazil',
'BSD': 'Bahamas',
'BTN': 'Bhutan',
'BWP': 'Botswana',
'BYN': 'Belarus',
'BZD': 'Belize',
'CAD': 'Canada',
'CDF': 'Democratic Republic of the Congo',
'CHF': 'Switzerland',
'CLP': 'Chile',
'CNY': 'China',
'COP': 'Colombia',
'CRC': 'Costa Rica',
'CUP': 'Cuba',
'CVE': 'Cape Verde',
'CZK': 'Czech Republic',
'DJF': 'Djibouti',
'DKK': 'Denmark',
'DOP': 'Dominican Republic',
'DZD': 'Algeria',
'EGP': 'Egypt',
'ERN': 'Eritrea',
'ETB': 'Ethiopia',
'EUR': 'Euro',
'FKP': 'Falkland Islands',
'FOK': 'Faroe Islands',
'GBP': 'United Kingdom',
'GEL': 'Georgia',
'GGP': 'Guernsey',
'GHS': 'Ghana',
'GIP': 'Gibraltar',
'GMD': 'The Gambia',
'GNF': 'Guinea',
'GTQ': 'Guatemala',
'GYD': 'Guyana',
'HKD': 'Hong Kong',
'HNL': 'Honduras',
'HRK': 'Croatia',
'HTG': 'Haiti',
'HUF': 'Hungary',
'IDR': 'Indonesia',
'ILS': 'Israel',
'IMP': 'Isle of Man',
'INR': 'India',
'IQD': 'Iraq',
'IRR': 'Iran',
'ISK': 'Iceland',
'JMD': 'Jamaica',
'JOD': 'Jordan',
'JPY': 'Japan',
'KES': 'Kenya',
'KGS': 'Kyrgyzstan',
'KHR': 'Cambodia',
'KID': 'Kiribati',
'KMF': 'Comoros',
'KRW': 'South Korea',
'KWD': 'Kuwait',
'KYD': 'Cayman Islands',
'KZT': 'Kazakhstan',
'LAK': 'Laos',
'LBP': 'Lebanon',
'LKR': 'Sri Lanka',
'LRD': 'Liberia',
'LSL': 'Lesotho',
'LYD': 'Libya',
'MAD': 'Morocco',
'MDL': 'Moldova',
'MGA': 'Madagascar',
'MKD': 'North Macedonia',
'MMK': 'Myanmar',
'MNT': 'Mongolia',
'MOP': 'Macau',
'MRU': 'Mauritania',
'MUR': 'Mauritius',
'MVR': 'Maldives',
'MWK': 'Malawi',
'MXN': 'Mexico',
'MYR': 'Malaysia',
'MZN': 'Mozambique',
'NAD': 'Namibia',
'NGN': 'Nigeria',
'NIO': 'Nicaragua',
'NOK': 'Norway',
'NPR': 'Nepal',
'NZD': 'New Zealand',
'OMR': 'Oman',
'PAB': 'Panama',
'PEN': 'Peru',
'PGK': 'Papua New Guinea',
'PHP': 'Philippines',
'PKR': 'Pakistan',
'PLN': 'Poland',
'PYG': 'Paraguay',
'QAR': 'Qatar',
'RON': 'Romania',
'RSD': 'Serbia',
'RUB': 'Russia',
'RWF': 'Rwanda',
'SAR': 'Saudi Arabia',
'SBD': 'Solomon Islands',
'SCR': 'Seychelles',
'SDG': 'Sudan',
'SEK': 'Sweden',
'SGD': 'Singapore',
'SHP': 'Saint Helena',
'SLL': 'Sierra Leone',
'SOS': 'Somalia',
'SRD': 'Suriname',
'SSP': 'South Sudan',
'STN': 'São Tomé and Príncipe',
'SYP': 'Syria',
'SZL': 'Eswatini',
'THB': 'Thailand',
'TJS': 'Tajikistan',
'TMT': 'Turkmenistan',
'TND': 'Tunisia',
'TOP': 'Tonga',
'TRY': 'Turkey',
'TTD': 'Trinidad and Tobago',
'TVD': 'Tuvalu',
'TWD': 'Taiwan',
'TZS': 'Tanzania',
'UAH': 'Ukraine',
'UGX': 'Uganda',
'USD': 'United States',
'UYU': 'Uruguay',
'UZS': 'Uzbekistan',
'VES': 'Venezuela',
'VND': 'Vietnam',
'VUV': 'Vanuatu',
'WST': 'Samoa',
'XCD': 'Organisation of Eastern Caribbean States',
'XDR': 'International Monetary Fund',
'YER': 'Yemen',
'ZAR': 'South Africa',
'ZMW': 'Zambia'}


def currency_check():
    valid = False
    currency_code = []
    while valid == False:
        try:
            curr = input('>> ')
            for code, country in codes.items():
                if curr.upper() == code or curr.upper() == country.upper():
                    valid = True
                    return code
                else:
                    currency_code.append(code)
                    if len(currency_code) == 155:
                        print('You need to use currency code or country name.')
        except TypeError:
            print('You need to use currency code or country name.')

def exchange_amount():
    valid = False
    while valid == False:
        try:
            exchange = int(input('How much would you like to exchange? '))
            if exchange > 0:
                valid = True
                return exchange
            else:
                print('The amount must be a positive number.')
        except ValueError:
            print('The amount must be a positive number.')

def exchange_check():
    print('Type choose currency code or country.')
    print('For European Union countries with Euro, choose Euro.')
    print('What currency do you have? ')
    first = currency_check()
    print('What currency would you like exchange it to?')
    second = currency_check()
    amount = exchange_amount()

    conversion_rate = 0
    conversion_result = 0

    url = f'https://v6.exchangerate-api.com/v6/10919f4b3c43e958a483d78a/pair/{first}/{second}/{amount}'
    response = requests.get(url)
    data = response.json()

    for key, value in data.items():
        if key == 'conversion_result':
            conversion_result += value

    for key, value in data.items():
        if key == 'conversion_rate':
            conversion_rate += value

    print(f'''
    Currency from: {first}
    Currency To: {second}
    Amount: {amount}
    Conversion rate {conversion_rate}
    Result: {conversion_result}''')

if __name__ == '__main__':
    exchange_check()
