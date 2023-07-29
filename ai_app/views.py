from django.shortcuts import render
from .globals import openai
from .globals import os
from .globals import time

# Create your views here.
def chat_AI(request):
    
    start_time = time.time()
    # Just to avoid error or initializing the 'query_input_field' as string
    query_input_field = ''
    
    if request.method == 'POST':
        try:
            query_input_field = str(request.POST.get('query_input_field'))
        except:
            query_input_field = str('Unable to get data')

    #####################################################################
    # Apen AI code starts here
    #####################################################################
    try:
        # openai.api_key = os.getenv('OPENAI_API_KEY')
        openai.api_key = os.getenv('OPENAI_API_KEYS')
        # print(OPENAI_API_KEYS)
        response = openai.Completion.create(
            # model=          'text-davinci-003',
            model=          'text-davinci-002',
            prompt=         query_input_field,
            max_tokens=     4000 # Max is 4097 tokens you can use 
        )
        query_input_field = query_input_field.capitalize()

        try:
            output_answer = response['choices'][0]['text']
            # output_answer = output_answer.strip()
            # stripped_code_block = '\n'.join([line.strip() for line in output_answer.split('\n')])
            # output_answer = stripped_code_block
 
        except:
            output_answer = 'Unable to run the BOT'
            pass

        # Finding the length of words in the response
        length_of_output_answer = output_answer.strip().split()  
        length_of_output_answer = len(length_of_output_answer)

        # Finding the length of words in the response
        end_time = time.time()
        final_time = end_time - start_time
        time_taken_output_time_in_seconds = int(final_time)
        time_taken_output_time_in_hh_mm_ss = time.strftime("%H:%M:%S", time.gmtime(time_taken_output_time_in_seconds))        
    except:
        query_input_field = query_input_field
        length_of_output_answer = ''
        time_taken_output_time_in_hh_mm_ss = ''
        output_answer = query_input_field
    
    # Context for passing values from views to html page
    context = {
        'your_entered_query' : query_input_field,
        'length_of_output_answer' : length_of_output_answer,
        'final_time': time_taken_output_time_in_hh_mm_ss,
        'output_answer': output_answer,
    }
    return render(request, 'chat_AI.html', context)


















