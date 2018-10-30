import os
import requests
import copy
import datetime

help_str = "Please format individual entries as 'chapter.section.problem'\n\nYou may do batch generation in the form:\n\nchapter[section(problem, problem, problem)]"
submission_overview_url = "https://app.crowdmark.com/student/courses/cse-260-discrete-structures"
student_name = ""
depends = []
submission_index = []

class individual_submission( object ):
    def __init__( self, problem_number, submission_address, depends, mp="template.tex" ):
        self.problem_number = str( problem_number )
        self.dependencies = depends

        #write function to actually grab this later
        self.submission_address = submission_address

        #Uses our generate_tex function to convert our template into a more
        #   easily operable string
        self.tex_str = ""#generate_tex( temp, problem_number, depends )

        #We'll refer to these when returning specific problem info
        self.dot_1 = self.problem_number.find( '.' )
        self.dot_3 = self.problem_number.rfind( '.')

    def generate_tex( template_fp, submission_index, depends ):
        #Imports our template file
        with open(template_fp) as t: content = t.readlines()

        tex_str = template_str
        date = datetime.datetime.now()

        tex_file = open("{}.tex".format("template_str"), "w+")


        for s in submission_index:
            #Replaces all relevant information in our tex string
            tex_str.replace( "@prob_num@", s )
            tex_str.replace( "@user_name@", student_name )
            tex_str.replace( "@current_date@", date.strftime("%m-%d-%Y") )

            #Generates our final .tex file
            tex_file = open("{}.tex".format("template_str"), "w+")
            tex_file.write( tex_str )
            tex_file.close()

            '''PACKAGE MANAGEMENT SUPPORT COMING SOON'''

    def problem_change( new_submission_str ):
        self.problem_number = new_submission_str

    def reset( self ):
        #Simply re-initalizes an contentless tex file
        self.tex_str = generate_tex( temp, problem_number, depends )

    def duplicate_submission( new_submission_str ):
        new_submission = copy.deepcopy( self )
        new_submission.problem_change( new_submission_str )

        return new_submission

    def render( self ):
        #Constructs the string we will pass to our OS shell
        render_cmd = "pdflatex" + problem_number + ".tex"

        #Tries to run our command, throws an error if it doesn't work
        try:
            os.system( render_cmd )
        except:
            print( "This only works on Linux, for now. Sorry!")


    '''I'll write these functions when I get to the the submission stuff'''
    def get_submission_address():
        pass

    def submit( self ):
        pass

    '''The following three functions simply use string parsing to return
        information about our submission possision'''

    def get_ch_num( self ):
        return int( self.problem_number[ :self.dot_1 ] )

    def get_sec_num( self ):
        return int( self.problem_number[ self.dot_2:self.dot_3])

    def get_prob_num( self ):
        return int( self.problem_number[ :self.dot_3 ] )

def get_depends():
    #Stores any additional needed packages in a list
    depends = []
    depends = str( input("\nPlease enter any additional necessary LaTeX packages seperated by commas: ")).split(",")
    #**ERROR CHECKING COMING SOON**

    return depends

def get_problem_nums():
    hw_index = []

    print( "Enter your problem numbers (enter D when finished)\nH for help")

    user_input = 'a'

    #Just a really ugly block of code that parses batch problem input
    while user_input != "d":
        user_input = str( input( ">" ) ).lower()

        if user_input == "h":
            print( help_str )
        elif "[" in user_input:
            prev_num = ""
            section = ""
            prev_list = []

            for c in user_input:
                if c == "[":
                    hw_index.append( prev_num )
                    prev_num = ""
                elif c in ",)":
                    prev_list.append( prev_num )

                    if c == ")":
                        hw_index.append( (int( section ), prev_list) )
                        section = ""
                        prev_list = []

                    prev_num = ""

                elif c == "(":
                    section = prev_num
                    prev_num = ""

                elif c.isnumeric():
                    prev_num += c


            user_input = "d"
        else:
            hw_index.append( str( user_input ) )

    return hw_index


def get_submission_index( assignment_index, depends ):
    ch = ""
    sec = ""
    problem_str = ""

    #We will store all of our refined problem number strings here
    submission_index = []

    #Run this block of code to expand encoded information
    if '.' not in assignment_index[0]:
        for index, itr in enumerate( assignment_index ):
            if index % 2 == 0:
                #Our chapter numbers are every even position in our list
                ch = itr
            else:
                sec = itr[0]

                for c in itr[1]:
                    submission_index.append( "{}.{}.{}".format( ch, sec, c ) )
    else:
        #Adds non-ecoded strings to our list
        [ submission_index.append( pn ) for pn in assignment_index ]
        #**ERROR CHECKING COMING SOON**

    return submission_index

def select_new():
    user_input = "s"

print( "Hello, good luck on your homework!\nEnter Q to quit\n\n**THIS PROGRAM DOES NOT DO YOUR HOMEWORK, IT IS ONLY CAPABLE OF FILE GENERATION AND SUBMISSION AUTOMATION**\n\n" )
student_name = input("Please enter your full name (used for submission attribution): ")

depends = get_depends()
submission_index = get_submission_index( get_problem_nums(), depends )

assignment = {}
commands = { 0:generate_tex,1:reset,2:duplicate_submission,3:render,4:submit,5:select_new }

for item in submission_index:
    assignment[item] = individual_submission( item, "placeholder", depends)

user_input = "s"
selected_problem = ""

while user_input != "q":
    ''''This prompts the user to enter the next problem they want
        to work with'''
    if user_input == "s":
        #Prints an ordered list of available problems
        for position, item in enumerate( submission_index ):
            if position == 0: print("\n")
            print( "[{}] {}".format( position, item ) )

        user_input = input("\n\n^^Please select a submmission^^\n(Select by position or name): ")

        #Parses user input for index or name selection then selects the problem
        if user_input.isnumeric():
            if int(user_input) <= assignment_index.len() and int(user_input) >= 0:
                selected_problem = assignment_index[int(user_input)]
            else:
                pass
        elif user_input in assignment_index:
            selected_problem = user_input
            user_input = "u"
        else:
            print("\n**Please make a valid selection.**")

    elif user_input == "u":
        for i, n in commands:
            print( "[{}] {}".format(i, str(n) ) )
