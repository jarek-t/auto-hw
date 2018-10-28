import os
import requests

submission_overview_url = "https://app.crowdmark.com/student/courses/cse-260-discrete-structures"
student_name = ""
dependencies = []

#turns out that might not be useful
#class Assignment( object ):
    def __init__( self, location, submission_address ):
        self.location = str( location )

        #Define function to actually grab this later
        self.submission_address = submission_address

    def duplicate( self, old_prob_num, new_prob_num ):
        pass;

    def get_ch_num( self ):
        pass;

    def get_sec_num( self ):
        pass;

class individual_submission( object ):
    def __init__( self, problem_number, submission_address ):
        self.problem_number = str( problem_number )
        #write function to actually grab this later
        self.submission_address = submission_address




    def reset( self ):
        pass

    def submit( self ):
        pass

    def render( self ):
        pass

    def get_ch_num( self ):
        pass

    def get_sec_num( self ):
        pass

    def get_ind_prob_num( self ):
        pass
