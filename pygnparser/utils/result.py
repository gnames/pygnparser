class Result(dict):
    def __init__(self, parsed_result):
        super().__init__()
        self.parsed_result = parsed_result
        self.update(parsed_result)


    def get_key(self, key, dict=None):
        if dict is None:
            dict = self.parsed_result
        try:
            key = dict[key]
        except KeyError:
            key = None
        return key

    
    def parsed(self):
        return self.get_key('parsed')


    def get_canonical(self):
        return self.get_key('canonical')

    
    def get_canonical_stemmed(self):
        return self.get_key('stemmed', dict=self.get_canonical())

    
    def get_canonical_simple(self):
        return self.get_key('simple', dict=self.get_canonical())

    
    def get_canonical_full(self):
        return self.get_key('full', dict=self.get_canonical())


    def get_authorship_details(self):
        return self.get_key('authorship')

    
    def get_authorship_verbatim(self):
        return self.get_key('verbatim', dict=self.get_authorship_details())

    
    def get_authorship_normalized(self):
        return self.get_key('normalized', dict=self.get_authorship_details())

    
    def get_authorship_year(self):
        return self.get_key('year', dict=self.get_authorship_details())

    
    def get_page(self):
        verbatim_authorship = self.get_authorship_verbatim()
        if ':' in verbatim_authorship:
            page = verbatim_authorship.split(':')[-1].strip()
        else:
            page = None
        return page

    
    def _format_authorship(self, authorship_details):
        authorship_list = authorship_details['authors']
        match len(authorship_list):
            case 0:
                authorship = ""
            case 1:
                authorship = authorship_list[0]
            case 2:
                authorship = f'{authorship_list[0]} & {authorship_list[1]}'
            case _:
                authorship = ', '.join(authorship_list[:-1]) + f' & {authorship_list[-1]}'
        if 'year' in authorship_details:
            year = self.get_key('year', dict=authorship_details['year'])
            authorship += f', {year}'
        if 'exAuthors' in authorship_details:
            ex_authorship = self._format_authorship(authorship_details['exAuthors'])
            authorship += f' in {ex_authorship}'
        return authorship

    
    def get_authorship(self):
        authorship_details = self.get_authorship_details()
        authorship = None
        if authorship_details is not None:
            if 'originalAuth' in authorship_details:
                authorship = self._format_authorship(authorship_details['originalAuth'])
            if 'combinationAuth' in authorship_details:
                combination_authorship = self._format_authorship(authorship_details['combinationAuth'])
                authorship = f'({authorship}) {combination_authorship}'

            # handles zoological authorship
            if 'combinationAuth' not in authorship_details and '(' in self.get_authorship_verbatim():
                authorship = f'({authorship})'
        return authorship


    def get_year(self):
        return self.get_authorship_year()


    def get_details(self):
        return self.get_key('details')


    def _get_details_rank(self):
        return list(self.get_details().keys())[0]


    def get_words(self):
        return self.get_key('words')


    def get_parser_version(self):
        return self.get_key('parserVersion')


    def get_id(self):
        return self.get_key('id')


    def get_verbatim(self):
        return self.get_key('verbatim')


    def get_normalized(self):
        return self.get_key('normalized')


    def get_quality(self):
        return self.get_key('quality')


    def get_cardinality(self):
        return self.get_key('cardinality')


    def get_tail(self):
        return self.get_key('tail')


    def get_quality_warnings(self):
        return self.get_key('qualityWarnings')


    def get_species(self):
        return self.get_key('species')


    def get_genus(self):
        return self.get_key('genus', dict=self.get_details()[self._get_details_rank()])


    def get_subgenus(self):
        return self.get_key('subgenus', dict=self.get_details()[self._get_details_rank()])


    def get_species(self):
        return self.get_key('species', dict=self.get_details()[self._get_details_rank()])


    def get_infraspecies_details(self):
        return self.get_key('infraspecies', dict=self.get_details()[self._get_details_rank()])


    def get_infraspecies(self):
        infraspecies_details = self.get_infraspecies_details()
        if infraspecies_details is not None:
            return self.get_key('value', dict=infraspecies_details[0])
        else:
            return None


    def get_infraspecies_rank(self):
        if self._get_details_rank() == 'infraspecies':
            rank = None
            if self.get_key('rank', dict=self.get_details()[self._get_details_rank()]['infraspecies'][0]) is not None:
                rank = self.get_key('rank', dict=self.get_details()[self._get_details_rank()]['infraspecies'][0])
        return rank


    def __str__(self):
            return self.parsed_result
