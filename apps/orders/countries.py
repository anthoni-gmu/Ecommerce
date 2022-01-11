from django.db import models


class Countries(models.TextChoices):
    Afghanistan = 'Afghanistan',
    Åland_Islands = 'Åland Islands',
    Albania = 'Albania',
    Algeria = 'Algeria',
    American_Samoa = 'American Samoa',
    Andorra = 'Andorra',
    Angola = 'Angola',
    Anguilla = 'Anguilla',
    Antarctica = 'Antarctica',
    Antigua_and_Barbuda = 'Antigua and Barbuda',
    Argentina = 'Argentina',
    Armenia = 'Armenia',
    Aruba = 'Aruba',
    Australia = 'Australia',
    Austria = 'Austria',
    Azerbaijan = 'Azerbaijan',
    Bahamas = 'Bahamas',
    Bahrain = 'Bahrain',
    Bangladesh = 'Bangladesh',
    Barbados = 'Barbados',
    Belarus = 'Belarus',
    Belgium = 'Belgium',
    Belize = 'Belize',
    Benin = 'Benin',
    Bermuda = 'Bermuda',
    Bhutan = 'Bhutan',
    Bolivia = 'Bolivia (Plurinational State of)',
    Bonaire = 'Bonaire, Sint Eustatius and Saba',
    Bosnia_and_Herzegovina = 'Bosnia and Herzegovina',
    Botswana = 'Botswana',
    Bouvet_Island = 'Bouvet Island',
    Brazil = 'Brazil',
    British_Indian_Ocean_Territory = 'British Indian Ocean Territory',
    Brunei_Darussalam = 'Brunei Darussalam',
    Bulgaria = 'Bulgaria',
    Burkina_Faso = 'Burkina Faso',
    Burundi = 'Burundi',
    Cabo_Verde = 'Cabo Verde',
    Cambodia = 'Cambodia',
    Cameroon = 'Cameroon',
    Canada = 'Canada',
    Cayman_Islands = 'Cayman Islands',
    Central_African_Republic = 'Central African Republic',
    Chad = 'Chad',
    Chile = 'Chile',
    China = 'China',
    Christmas_Island = 'Christmas Island',
    Cocos_Islands = 'Cocos (Keeling) Islands',
    Colombia = 'Colombia',
    Comoros = 'Comoros',
    Congo = 'Congo',
    Democratic_Republic_of_the_Congo = 'Democratic Republic of the Congo',
    Cook_Islands = 'Cook Islands',
    Costa_Rica = 'Costa Rica',
    Côte_dIvoire = "Côte d'Ivoire",
    Croatia = 'Croatia',
    Cuba = 'Cuba',
    Curaçao = 'Curaçao',
    Cyprus = 'Cyprus',
    Czechia = 'Czechia',
    Denmark = 'Denmark',
    Djibouti = 'Djibouti',
    Dominica = 'Dominica',
    Dominican_Republic = 'Dominican Republic',
    Ecuador = 'Ecuador',
    Egypt = 'Egypt',
    El_Salvador = 'El Salvador',
    Equatorial_Guinea = 'Equatorial Guinea',
    Eritrea = 'Eritrea',
    Estonia = 'Estonia',
    Eswatini = 'Eswatini',
    Ethiopia = 'Ethiopia',
    Falkland_Islands = 'Falkland Islands (Malvinas)',
    Faroe_Islands = 'Faroe Islands',
    Fiji = 'Fiji',
    Finland = 'Finland',
    France = 'France',
    French_Guiana = 'French Guiana',
    French_Polynesia = 'French Polynesia',
    French_Southern_Territories = 'French Southern Territories',
    Gabon = 'Gabon',
    Gambia = 'Gambia',
    Georgia = 'Georgia',
    Germany = 'Germany',
    Ghana = 'Ghana',
    Gibraltar = 'Gibraltar',
    Greece = 'Greece',
    Greenland = 'Greenland',
    Grenada = 'Grenada',
    Guadeloupe = 'Guadeloupe',
    Guam = 'Guam',
    Guatemala = 'Guatemala',
    Guernsey = 'Guernsey',
    Guinea = 'Guinea',
    Guinea_Bissau = 'Guinea-Bissau',
    Guyana = 'Guyana',
    Haiti = 'Haiti',
    Heard_Island_and_McDonald_Islands = 'Heard Island and McDonald Islands',
    Holy_See = 'Holy See',
    Honduras = 'Honduras',
    Hong_Kong = 'Hong Kong',
    Hungary = 'Hungary',
    Iceland = 'Iceland',
    India = 'India',
    Indonesia = 'Indonesia',
    Iran = 'Iran (Islamic Republic of)',
    Iraq = 'Iraq',
    Ireland = 'Ireland',
    Isle_of_Man = 'Isle of Man',
    Israel = 'Israel',
    Italy = 'Italy',
    Jamaica = 'Jamaica',
    Japan = 'Japan',
    Jersey = 'Jersey',
    Jordan = 'Jordan',
    Kazakhstan = 'Kazakhstan',
    Kenya = 'Kenya',
    Kiribati = 'Kiribati',
    Democratic_Peoples_Republic_of_Korea = "Korea (the Democratic People's Republic of)",
    Republic_of_Korea = 'Korea (the Republic of)',
    Kuwait = 'Kuwait',
    Kyrgyzstan = 'Kyrgyzstan',
    Lao_Peoples_Democratic_Republic = "Lao People's Democratic Republic",
    Latvia = 'Latvia',
    Lebanon = 'Lebanon',
    Lesotho = 'Lesotho',
    Liberia = 'Liberia',
    Libya = 'Libya',
    Liechtenstein = 'Liechtenstein',
    Lithuania = 'Lithuania',
    Luxembourg = 'Luxembourg',
    Macao = 'Macao',
    Madagascar = 'Madagascar',
    Malawi = 'Malawi',
    MalaysiaMY = 'Malaysia',
    Maldives = 'Maldives',
    Mali = 'Mali',
    Malta = 'Malta',
    Marshall_Islands = 'Marshall Islands',
    Martinique = 'Martinique',
    Mauritania = 'Mauritania',
    Mauritius = 'Mauritius',
    Mayotte = 'Mayotte',
    Mexico = 'Mexico',
    Micronesia = 'Micronesia (Federated States of)',
    Moldova = 'Moldova (the Republic of)',
    Monaco = 'Monaco',
    Mongolia = 'Mongolia',
    Montenegro = 'Montenegro',
    Montserrat = 'Montserrat',
    Morocco = 'Morocco',
    Mozambique = 'Mozambique',
    Myanmar = 'Myanmar',
    Namibia = 'Namibia',
    Nauru = 'Nauru',
    Nepal = 'Nepal',
    Netherlands = 'Netherlands',
    New_Caledonia = 'New Caledonia',
    New_Zealand = 'New Zealand',
    Nicaragua = 'Nicaragua',
    Niger = 'Niger',
    Nigeria = 'Nigeria',
    Niue = 'Niue',
    Norfolk_Island = 'Norfolk Island',
    North_Macedonia = 'North Macedonia',
    Northern_Mariana_Islands = 'Northern Mariana Islands',
    Norway = 'Norway',
    Oman = 'Oman',
    Pakistan = 'Pakistan',
    Palau = 'Palau',
    Palestine = 'Palestine, State of',
    Panama = 'Panama',
    Papua_New_Guinea = 'Papua New Guinea',
    Paraguay = 'Paraguay',
    Peru = 'Peru',
    Philippines = 'Philippines',
    Pitcairn = 'Pitcairn',
    Poland = 'Poland',
    Portugal = 'Portugal',
    Puerto_Rico = 'Puerto Rico',
    Qatar = 'Qatar',
    Réunion = 'Réunion',
    Romania = 'Romania',
    Russian_Federation = 'Russian Federation',
    Rwanda = 'Rwanda',
    Saint_Barthélemy = 'Saint Barthélemy',
    Saint_Helena = 'Saint Helena, Ascension and Tristan da Cunha',
    Saint_Kitts_and_Nevis = 'Saint Kitts and Nevis',
    Saint_Lucia = 'Saint Lucia',
    Saint_Martin = 'Saint Martin (French part)',
    Saint_Pierre_and_Miquelon = 'Saint Pierre and Miquelon',
    Saint_Vincent_and_the_Grenadines = 'Saint Vincent and the Grenadines',
    Samoa = 'Samoa',
    San_Marino = 'San Marino',
    Sao_Tome_and_Principe = 'Sao Tome and Principe',
    Saudi_Arabia = 'Saudi Arabia',
    Senegal = 'Senegal',
    Serbia = 'Serbia',
    Seychelles = 'Seychelles',
    Sierra_Leone = 'Sierra Leone',
    Singapore = 'Singapore',
    Sint_Maarten = 'Sint Maarten (Dutch part)',
    Slovakia = 'Slovakia',
    Slovenia = 'Slovenia',
    Solomon_Islands = 'Solomon Islands',
    Somalia = 'Somalia',
    South_Africa = 'South Africa',
    South_Georgia_and_the_South_Sandwich_Islands = 'South Georgia and the South Sandwich Islands',
    South_Sudan = 'South Sudan',
    Spain = 'Spain',
    Sri_Lanka = 'Sri Lanka',
    Sudan = 'Sudan',
    Suriname = 'Suriname',
    Svalbard_and_Jan_Mayen = 'Svalbard and Jan Mayen',
    Sweden = 'Sweden',
    Switzerland = 'Switzerland',
    Syrian_Arab_Republic = 'Syrian Arab Republic',
    Taiwan = 'Taiwan (Province of China)',
    Tajikistan = 'Tajikistan',
    Tanzania = 'Tanzania, the United Republic of',
    Thailand = 'Thailand',
    Timor_Leste = 'Timor-Leste',
    Togo = 'Togo',
    Tokelau = 'Tokelau',
    Tonga = 'Tonga',
    Trinidad_and_Tobago = 'Trinidad and Tobago',
    Tunisia = 'Tunisia',
    Turkey = 'Turkey',
    Turkmenistan = 'Turkmenistan',
    Turks_and_Caicos_Islands = 'Turks and Caicos Islands',
    Tuvalu = 'Tuvalu',
    Uganda = 'Uganda',
    Ukraine = 'Ukraine',
    United_Arab_Emirates = 'United Arab Emirates',
    United_Kingdom_of_Great_Britain_and_Northern_Ireland = 'United Kingdom of Great Britain and Northern Ireland',
    United_States_Minor_Outlying_Islands = 'United States Minor Outlying Islands',
    United_States_of_America = 'United States of America',
    Uruguay = 'Uruguay',
    Uzbekistan = 'Uzbekistan',
    Vanuatu = 'Vanuatu',
    Venezuela = 'Venezuela (Bolivarian Republic of)',
    Viet_Nam = 'Viet Nam',
    British_Virgin_Islands = 'Virgin Islands (British)',
    US_Virgin_Islands = 'Virgin Islands (U.S.)',
    Wallis_and_Futuna = 'Wallis and Futuna',
    Western_Sahara = 'Western Sahara',
    Yemen = 'Yemen',
    Zambia = 'Zambia',
    Zimbabwe = 'Zimbabwe'