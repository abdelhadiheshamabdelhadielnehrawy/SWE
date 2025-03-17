
"""
A text analysis program that provides statistics about given text.
"""

class TextAnalyzer:
    """
    Analyzes text and provides statistics about words, characters, and so on.
    """
    
    MAX_TEXT_LENGTH = 1000  # Maximum allowed characters in text
    SPECIAL_CHARS = "!@#$%^&*()_+-=[]{}|;:,.<>?'\"`~"

    def _init_(self):
        """Initialize the TextAnalyzer"""
        pass

    def analyzeText(self, inputText: str) -> dict:
        """
        Analyze the given text and return statistics.

        Args:
            inputText (str): The text to analyze

        Returns:
            dict: Dictionary containing text analysis statistics
        """
        try:
            if not inputText:
                raise ValueError("Input text cannot be empty")
            
            if len(inputText) > self.MAX_TEXT_LENGTH:
                raise ValueError(f"Text exceeds maximum length of {self.MAX_TEXT_LENGTH}")
            
            # Calculate statistics
            wordCount = len(inputText.split())
            charCount = len(inputText)
            whitespaceCount = inputText.count(' ')
            numberCount = sum(c.isdigit() for c in inputText)
            specialCharCount = sum(c in self.SPECIAL_CHARS for c in inputText)
            letterCount = sum(c.isalpha() for c in inputText)

            return {
                "wordCount": wordCount,
                "charCount": charCount,
                "letterCount": letterCount,
                "numberCount": numberCount,
                "specialCharCount": specialCharCount,
                "whitespaceCount": whitespaceCount
            }

        except Exception as e:
            print(f"Error analyzing text: {str(e)}")
            return {
                "error": str(e)
            }

def main():
    """Main function to demonstrate TextAnalyzer usage."""
    analyzer = TextAnalyzer()
    
    # Test case 1: Normal text
    sampleText1 = "Hello World! 123 #testing"
    result1 = analyzer.analyzeText(sampleText1)
    print("Analysis 1:")
    for key, value in result1.items():
        print(f"{key}: {value}")
    
    # Test case 2: Text with various characters
    sampleText2 = "User123@email.com has 2 items!!"
    result2 = analyzer.analyzeText(sampleText2)
    print("\nAnalysis 2:")
    for key, value in result2.items():
        print(f"{key}: {value}")

    # Test case 2: Text with various characters
    sampleText3 = "A"*1001
    result3 = analyzer.analyzeText(sampleText3)
    print("\nAnalysis 3:")
    for key, value in result3.items():
        print(f"{key}: {value}")
if __name__ == "__main__":
    main()