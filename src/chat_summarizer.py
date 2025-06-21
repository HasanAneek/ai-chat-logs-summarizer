import os
from typing import Dict, List, Tuple
import sys

class ChatSummarizer:
    def parse_chat_log(self, file_path: str) -> Tuple[List[str], List[str]]:
        """
        Parse the chat log file and separate messages by speaker.
        """
        user_messages = []
        ai_messages = []
        
        try:
            with open(file_path, 'r', encoding='utf-8') as file:
                for line in file:
                    line = line.strip()
                    if line.startswith('User:'):
                        user_messages.append(line[6:].strip())
                    elif line.startswith('AI:'):
                        ai_messages.append(line[4:].strip())
        except FileNotFoundError:
            print(f"Error: File {file_path} not found.")
            return [], []
        except Exception as e:
            print(f"Error reading file: {str(e)}")
            return [], []
            
        return user_messages, ai_messages

    def get_message_statistics(self, user_messages: List[str], ai_messages: List[str]) -> Dict:
        """
        Calculate basic statistics about the chat.
        """
        return {
            'total_messages': len(user_messages) + len(ai_messages),
            'user_messages': len(user_messages),
            'ai_messages': len(ai_messages)
        }

def main():
    """Main function to demonstrate the ChatSummarizer functionality."""
    summarizer = ChatSummarizer()
    
    # Hardcoded path for now
    data_dir = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'data')
    chat_file = os.path.join(data_dir, 'chat.txt')
    
    user_messages, ai_messages = summarizer.parse_chat_log(chat_file)
    
    if user_messages or ai_messages:
        stats = summarizer.get_message_statistics(user_messages, ai_messages)
        
        print("\nChat Log Summary:")
        print(f"- Total exchanges: {stats['total_messages']}")
        print(f"- User messages: {stats['user_messages']}")
        print(f"- AI messages: {stats['ai_messages']}\n")

if __name__ == "__main__":
    main()