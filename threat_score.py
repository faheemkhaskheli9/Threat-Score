# TODO create class for threat score
class ThreatScore:

    def __init__(self):
        # person is object of people class
        self.person = None

        self.scores_list = []
        self.reasons_list = []

        # following are reason for which a person can be a threat to you.
        self.ReasonChoices = {"Personal": 1.0,
                              "Stuff": 1.0,
                              "Religion": 1.0,
                              "Race": 1.0,
                              "Nationality": 1.0,
                              "Gender": 1.0,
                              "Jealousy": 0.5,
                              "Steal": 0.5,
                              "Blocked": 0.5,
                              "Ignore": 0.5,
                              "Argue": 0.5,
                              "Inherit": 0.5}

    def count_threat_score(self):
        '''
        This function return the sum of all the threat score, it can be used to get overview
        of a person.
        :return:
        '''
        return sum(self.scores_list)

    def show_reasons(self, return_scores=True):
        '''
        This function will print the list of reason along with threat score
        :param return_scores: set it True if you want to see threat score for specific reason
        :return: None
        '''

        if return_scores:
            for r, s in zip(self.reasons_list, self.scores_list):
                print(r, s)
        else:
            for r in self.reasons_list:
                print(r)

    def add_reason(self, reason):
        '''
        You can add new threat score based on reason that are specified in the ReasonChoice list.
        :param reason: item from ReasonChoice
        :return:
        '''

        if reason in self.ReasonChoices:
            self.reasons_list.append(reason)
            self.scores_list.append(self.ReasonChoices[reason])
            print("Reason added to list", self.person.name, 'now has ',self.count_threat_score, 'Threat Score.')
        else:
            print("Please Select Reason From Default Reason Available")
