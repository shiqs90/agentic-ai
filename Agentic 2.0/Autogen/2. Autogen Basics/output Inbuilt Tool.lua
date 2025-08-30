[
    
    
    TextMessage(id='acbc7572-c9f8-4472-910c-a965f41a4bda', source='user', models_usage=None, metadata={}, created_at=datetime.datetime(2025, 7, 12, 3, 17, 56, 108397, tzinfo=datetime.timezone.utc), content='Give me a random cat fact', type='TextMessage'), 
    
    
    ToolCallRequestEvent(id='97ecc530-e635-4e16-a1a0-8b16ed9d5ff6', source='CatFactsAgent', models_usage=RequestUsage(prompt_tokens=98, completion_tokens=30), metadata={}, created_at=datetime.datetime(2025, 7, 12, 3, 18, 1, 51586, tzinfo=datetime.timezone.utc), content=[FunctionCall(id='call_PG59MGIrAqum7LEh1ZHaHxCK', arguments='{"fact":"Cats have whiskers on the backs of their front legs.","length":43}', name='cat_facts_api')], type='ToolCallRequestEvent'), 
    
    
    ToolCallExecutionEvent(id='0e8f5061-b20b-40fb-8526-de576575f3f4', source='CatFactsAgent', models_usage=None, metadata={}, created_at=datetime.datetime(2025, 7, 12, 3, 18, 2, 993815, tzinfo=datetime.timezone.utc), content=[FunctionExecutionResult(content="{'fact': 'Cats often overract to unexpected stimuli because of their extremely sensitive nervous system.', 'length': 94}", name='cat_facts_api', call_id='call_PG59MGIrAqum7LEh1ZHaHxCK', is_error=False)], type='ToolCallExecutionEvent'), 
    
    
    TextMessage(id='31b013ba-60b1-4091-a686-cd256f3c7871', source='CatFactsAgent', models_usage=RequestUsage(prompt_tokens=106, completion_tokens=31), metadata={}, created_at=datetime.datetime(2025, 7, 12, 3, 18, 4, 248170, tzinfo=datetime.timezone.utc), content="Here's a fun cat fact: Cats often overreact to unexpected stimuli due to their extremely sensitive nervous system. This sensitivity makes them more responsive to their surroundings.", type='TextMessage')

]