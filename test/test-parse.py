import vcr
import re
from pygnparser import gnparser


@vcr.use_cassette("test/vcr_cassettes/test_parse_Aus_cus_dus.yaml")
def test_version():
    res = gnparser('Aus bus cus (Smith, 1999)')
    assert re.match(r'v\d\.\d\.\d', res.get_parser_version())


@vcr.use_cassette("test/vcr_cassettes/test_parse_Aus_cus_dus.yaml")
def test_id():
    res = gnparser('Aus bus cus (Smith, 1999)')
    assert res.get_id() == '4909dd2f-acc2-558f-b8f3-74a975a120b7'


@vcr.use_cassette("test/vcr_cassettes/test_parse_Aus_cus_dus.yaml")
def test_parsed():
    res = gnparser('Aus bus cus (Smith, 1999)')
    assert res.parsed() is True


@vcr.use_cassette("test/vcr_cassettes/test_parse_Aus_cus_dus.yaml")
def test_cardinality():
    res = gnparser('Aus bus cus (Smith, 1999)')
    assert res.get_cardinality() == 3


@vcr.use_cassette("test/vcr_cassettes/test_parse_Aus_cus_dus.yaml")
def test_parse_quality():
    res = gnparser('Aus (Bus) cus dus (Smith, 1980)')
    assert res.get_quality() == 1


@vcr.use_cassette("test/vcr_cassettes/test_parse_Aus_cus_dus.yaml")
def test_verbatim():
    res = gnparser('Aus (Bus) cus dus (Smith, 1980)')
    assert res.get_verbatim() == 'Aus (Bus) cus dus (Smith, 1980)'


@vcr.use_cassette("test/vcr_cassettes/test_parse_Aus_cus_dus.yaml")
def test_normalized():
    res = gnparser('Aus (Bus) cus dus (Smith, 1980)')
    assert res.get_normalized() == 'Aus (Bus) cus dus (Smith 1980)'


@vcr.use_cassette("test/vcr_cassettes/test_parse_Aus_cus_dus.yaml")
def test_canonical():
    res = gnparser('Aus (Bus) cus dus (Smith, 1980)')
    assert res.get_canonical() == {'stemmed': 'Aus cus dus', 'simple': 'Aus cus dus', 'full': 'Aus cus dus'}


@vcr.use_cassette("test/vcr_cassettes/test_parse_Aus_cus_dus.yaml")
def test_canonical_stemmed():
    res = gnparser('Aus (Bus) cus dus (Smith, 1980)')
    assert res.get_canonical_stemmed() == 'Aus cus dus'


@vcr.use_cassette("test/vcr_cassettes/test_parse_Aus_cus_dus.yaml")
def test_canonical_simple():
    res = gnparser('Aus (Bus) cus dus (Smith, 1980)')
    assert res.get_canonical_simple() == 'Aus cus dus'


@vcr.use_cassette("test/vcr_cassettes/test_parse_Aus_cus_dus.yaml")
def test_canonical_full():
    res = gnparser('Aus (Bus) cus dus (Smith, 1980)')
    assert res.get_canonical_full() == 'Aus cus dus'


@vcr.use_cassette("test/vcr_cassettes/test_parse_Aus_cus_dus.yaml")
def test_authorship_details():
    res = gnparser('Aus (Bus) cus dus (Smith, 1980)')
    assert 'verbatim' in res.get_authorship_details()


@vcr.use_cassette("test/vcr_cassettes/test_parse_Aus_cus_dus.yaml")
def test_details():
    res = gnparser('Aus (Bus) cus dus (Smith, 1980)')
    assert 'infraspecies' in res.get_details()
    

@vcr.use_cassette("test/vcr_cassettes/test_parse_Aus_cus_dus.yaml")
def test_infraspecies_details():
    res = gnparser('Aus (Bus) cus dus (Smith, 1980)')
    assert 'value' in res.get_infraspecies_details()[0]


@vcr.use_cassette("test/vcr_cassettes/test_parse_Aus_cus_dus.yaml")
def test_words():
    res = gnparser('Aus (Bus) cus dus (Smith, 1980)')
    assert 'start' in res.get_words()[0]


@vcr.use_cassette("test/vcr_cassettes/test_parse_Aus_cus_dus.yaml")
def test_parse_genus():
    res = gnparser('Aus (Bus) cus dus (Smith, 1980)')
    assert res.get_genus() == 'Aus'


@vcr.use_cassette("test/vcr_cassettes/test_parse_Aus_cus_dus.yaml")
def test_parse_subgenus():
    res = gnparser('Aus (Bus) cus dus (Smith, 1980)')
    assert res.get_subgenus() == 'Bus'


@vcr.use_cassette("test/vcr_cassettes/test_parse_Aus_cus_dus.yaml")
def test_parse_species():
    res = gnparser('Aus (Bus) cus dus (Smith, 1980)')
    assert res.get_species() == 'cus'


@vcr.use_cassette("test/vcr_cassettes/test_parse_Aus_cus_dus.yaml")
def test_parse_infraspecies():
    res = gnparser('Aus (Bus) cus dus (Smith, 1980)')
    assert res.get_infraspecies() == 'dus'


@vcr.use_cassette("test/vcr_cassettes/test_parse_Aus_cus_dus.yaml")
def test_parse_infraspecies_rank():
    res = gnparser('Aus (Bus) cus dus (Smith, 1980)')
    assert res.get_infraspecies_rank() is None


@vcr.use_cassette("test/vcr_cassettes/test_parse_Aus_cus_var_dus.yaml")
def test_parse_infraspecies_var_rank():
    res = gnparser('Aus (Bus) cus var. dus (Smith, 1980)')
    assert res.get_infraspecies_rank() == 'var.'


@vcr.use_cassette("test/vcr_cassettes/test_parse_Aus_cus_dus.yaml")
def test_parse_authorship_verbatim():
    res = gnparser('Aus (Bus) cus dus (Smith, 1980)')
    assert res.get_authorship_verbatim() == '(Smith, 1980)'


@vcr.use_cassette("test/vcr_cassettes/test_parse_Aus_cus_dus.yaml")
def test_parse_authorship_normalized():
    res = gnparser('Aus (Bus) cus dus (Smith, 1980)')
    assert res.get_authorship_normalized() == '(Smith 1980)'


@vcr.use_cassette("test/vcr_cassettes/test_parse_Aus_cus_dus.yaml")
def test_parse_authorship_year():
    res = gnparser('Aus (Bus) cus dus (Smith, 1980)')
    assert res.get_authorship_year() == '1980'


@vcr.use_cassette("test/vcr_cassettes/test_parse_Aus_cus_dus.yaml")
def test_parse_year():
    res = gnparser('Aus (Bus) cus dus (Smith, 1980)')
    assert res.get_year() == '1980'

@vcr.use_cassette("test/vcr_cassettes/test_parse_Aus_cus_dus.yaml")
def test_parse_authorship():
    res = gnparser('Aus (Bus) cus dus (Smith, 1980)')
    assert res.get_authorship() == '(Smith, 1980)'


@vcr.use_cassette("test/vcr_cassettes/test_parse_Naja_porphyrica.yaml")
def test_parse_Naja_porphyrica_genus():
    res = gnparser('Naja porphyrica SCHLEGEL 1837: 479 (in error pro Coluber porphyriacus)')
    assert res.get_genus() == 'Naja'


@vcr.use_cassette("test/vcr_cassettes/test_parse_Naja_porphyrica.yaml")
def test_parse_Naja_porphyrica_species():
    res = gnparser('Naja porphyrica SCHLEGEL 1837: 479 (in error pro Coluber porphyriacus)')
    assert res.get_species() == 'porphyrica'


@vcr.use_cassette("test/vcr_cassettes/test_parse_Naja_porphyrica.yaml")
def test_parse_Naja_porphyrica_tail():
    res = gnparser('Naja porphyrica SCHLEGEL 1837: 479 (in error pro Coluber porphyriacus)')
    assert res.get_tail() == ' (in error pro Coluber porphyriacus)'


@vcr.use_cassette("test/vcr_cassettes/test_parse_Naja_porphyrica.yaml")
def test_parse_Naja_porphyrica_authorship_verbatim():
    res = gnparser('Naja porphyrica SCHLEGEL 1837: 479 (in error pro Coluber porphyriacus)')
    assert res.get_authorship_verbatim() == 'SCHLEGEL 1837: 479'


@vcr.use_cassette("test/vcr_cassettes/test_parse_Naja_porphyrica.yaml")
def test_parse_Naja_porphyrica_authorship_normalized():
    res = gnparser('Naja porphyrica SCHLEGEL 1837: 479 (in error pro Coluber porphyriacus)')
    assert res.get_authorship_normalized() == 'Schlegel 1837'


@vcr.use_cassette("test/vcr_cassettes/test_parse_Naja_porphyrica.yaml")
def test_parse_Naja_porphyrica_authorship_year():
    res = gnparser('Naja porphyrica SCHLEGEL 1837: 479 (in error pro Coluber porphyriacus)')
    assert res.get_authorship_year() == '1837'


@vcr.use_cassette("test/vcr_cassettes/test_parse_Naja_porphyrica.yaml")
def test_parse_Naja_porphyrica_authorship():
    res = gnparser('Naja porphyrica SCHLEGEL 1837: 479 (in error pro Coluber porphyriacus)')
    assert res.get_authorship() == 'Schlegel, 1837'


@vcr.use_cassette("test/vcr_cassettes/test_parse_4_authors.yaml")
def test_parse_4_authors():
    res = gnparser('Aus bus cus (Smith, Anderson, Jones, & Ryan, 1999)')
    assert res.get_authorship() == '(Smith, Anderson, Jones & Ryan, 1999)'


@vcr.use_cassette("test/vcr_cassettes/test_parse_3_authors.yaml")
def test_parse_3_authors():
    res = gnparser('Aus bus cus (Smith, Anderson & Ryan, 1999)')
    assert res.get_authorship() == '(Smith, Anderson & Ryan, 1999)'


@vcr.use_cassette("test/vcr_cassettes/test_parse_3_authors_no_brackets.yaml")
def test_parse_3_authors_no_brackets():
    res = gnparser('Aus bus cus Smith, Anderson & Ryan, 1999')
    assert res.get_authorship() == 'Smith, Anderson & Ryan, 1999'


@vcr.use_cassette("test/vcr_cassettes/test_parse_2_authors.yaml")
def test_parse_2_authors():
    res = gnparser('Aus bus cus (Smith & Anderson, 1999)')
    assert res.get_authorship() == '(Smith & Anderson, 1999)'


@vcr.use_cassette("test/vcr_cassettes/test_parse_2_authors_no_brackets.yaml")
def test_parse_2_authors_no_brackets():
    res = gnparser('Aus bus cus Smith & Anderson, 1999')
    assert res.get_authorship() == 'Smith & Anderson, 1999'


@vcr.use_cassette("test/vcr_cassettes/test_parse_1_author.yaml")
def test_parse_1_author():
    res = gnparser('Aus bus cus (Smith, 1999)')
    assert res.get_authorship() == '(Smith, 1999)'


@vcr.use_cassette("test/vcr_cassettes/test_parse_1_author_no_brackets.yaml")
def test_parse_1_author_no_brackets():
    res = gnparser('Aus bus cus Smith, 1999')
    assert res.get_authorship() == 'Smith, 1999'


@vcr.use_cassette("test/vcr_cassettes/test_parse_ex_original.yaml")
def test_parse_ex_original():
    res = gnparser('Aus bus cus Smith in Richards, 1999')
    assert res.get_authorship() == 'Smith in Richards, 1999'


@vcr.use_cassette("test/vcr_cassettes/test_parse_ex_original_comb.yaml")
def test_parse_ex_original_comb():
    res = gnparser('Aus bus cus (Smith in Richards, 1999) Ryan in Anderson, Smith, & Jones, 2000')
    assert res.get_authorship() == '(Smith in Richards, 1999) Ryan in Anderson, Smith & Jones, 2000'


@vcr.use_cassette("test/vcr_cassettes/test_parse_Ablepharus_pannonicus.yaml")
def test_parse_Ablepharus_pannonicus():
    res = gnparser('Ablepharus pannonicus Fitzinger in Eversmann, 1823: 145 (Nom. Nud., In Error)')
    assert res.get_genus() == 'Ablepharus'
    assert res.get_species() == 'pannonicus'
    assert res.get_infraspecies() is None
    assert res.get_authorship() == 'Fitzinger in Eversmann, 1823'
    assert res.get_page() == '145'
    assert res.get_quality_warnings() == [{'quality': 4, 'warning': 'Unparsed tail'}, {'quality': 2, 'warning': 'Ex authors are not required (ICZN only)'}, {'quality': 2, 'warning': 'Year with page info'}]
    assert res.get_tail().strip() == '(Nom. Nud., In Error)'


@vcr.use_cassette("test/vcr_cassettes/test_parse_Aspidoscelis_neavesi.yaml")
def test_parse_Aspidoscelis_neavesi():
    res = gnparser('Aspidoscelis neavesi Cole, Taylor, Baumann & Baumann, 2014 (Part)')
    assert res.get_genus() == 'Aspidoscelis'
    assert res.get_species() == 'neavesi'
    assert res.get_infraspecies() is None
    assert res.get_authorship() == 'Cole, Taylor, Baumann & Baumann, 2014'
    assert res.get_page() is None
    assert res.get_tail().strip() == '(Part)'


@vcr.use_cassette("test/vcr_cassettes/test_parse_Atuechosaurus_travancoricus.yaml")
def test_parse_Atuechosaurus_travancoricus():
    res = gnparser('Atuechosaurus travancoricus Beddome, 1870: 33 (Part.)')
    assert res.get_genus() == 'Atuechosaurus'
    assert res.get_species() == 'travancoricus'
    assert res.get_infraspecies() is None
    assert res.get_authorship() == 'Beddome, 1870'
    assert res.get_page() == '33'
    assert res.get_tail().strip() == '(Part.)'


@vcr.use_cassette("test/vcr_cassettes/test_parse_Calyptoprymnus_verecundus.yaml")
def test_parse_Calyptoprymnus_verecundus():
    res = gnparser('Calyptoprymnus verecundus De Vis, 1905: 46 (Fide Moody, 1977)')
    assert res.get_genus() == 'Calyptoprymnus'
    assert res.get_species() == 'verecundus'
    assert res.get_infraspecies() is None
    assert res.get_authorship() == 'De Vis, 1905'
    assert res.get_page() == '46'
    assert res.get_tail().strip() == '(Fide Moody, 1977)'

