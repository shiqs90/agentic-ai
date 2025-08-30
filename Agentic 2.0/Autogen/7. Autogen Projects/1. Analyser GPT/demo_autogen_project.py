
from autogen_agentchat.conditions import TextMentionTermination
from autogen_agentchat.teams import RoundRobinGroupChat
from autogen_agentchat.ui import Console
from autogen_ext.models.openai import OpenAIChatCompletionClient

from agents.agents import planner_agent,local_agent,language_agent,travel_summary_agent


model_client = OpenAIChatCompletionClient(model="gpt-4o")



termination = TextMentionTermination("TERMINATE")
group_chat = RoundRobinGroupChat(
    [planner_agent, local_agent, language_agent, travel_summary_agent], termination_condition=termination
)
await Console(group_chat.run_stream(task="Plan a 3 day trip to Nepal."))

await model_client.close()
