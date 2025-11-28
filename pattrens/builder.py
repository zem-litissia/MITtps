from abc import ABC, abstractmethod
from typing import List, Optional

# Product
class Story:
    """Represent the complex object under construction."""
    
    def __init__(self):
        self.parts: List[str] = []
        
    def add(self, part: str):
        self.parts.append(part)
        
    def show(self):
        print(f"Story configuration: {self.parts}")

# Builder Interface
class StoryBuilder(ABC):
    """Specify an abstract interface for creating parts of a Product object."""
    
    def __init__(self):
        self.story = Story()
        
    @abstractmethod
    def _build_image(self):
        pass
        
    @abstractmethod
    def _build_music(self):
        pass
        
    @abstractmethod
    def _build_effect(self):
        pass
        
    @abstractmethod
    def _build_video(self):
        pass

# Concrete Builders
class FacebookConcreteBuilder(StoryBuilder):
    def _build_image(self):
        self.story.add("Facebook Photo")
            
    def _build_music(self):
        self.story.add("Facebook Music")
            
    def _build_effect(self):
        self.story.add("Facebook Effect")
            
    def _build_video(self):
        self.story.add("Facebook Video")

class InstagramConcreteBuilder(StoryBuilder):
    def _build_image(self):
        self.story.add("Instagram Photo")
            
    def _build_music(self):
        self.story.add("Instagram Music")
            
    def _build_effect(self):
        self.story.add("Instagram Filter")
            
    def _build_video(self):
        self.story.add("Instagram Video")

# Director
class StoryDirector:
    """Constructs stories using the builder."""
    
    def __init__(self):
        self.builder: Optional[StoryBuilder] = None
            
    def construct(self, builder: StoryBuilder):
        self.builder = builder
            
    def basic_story(self):
        """Creates a story with just a photo"""
        self.builder._build_image()
            
    def music_story(self):
        """Creates a story with photo and music"""
        self.builder._build_image()
        self.builder._build_music()
            
    def video_story(self):
        """Creates a story with video and effects"""
        self.builder._build_video()
        self.builder._build_effect()

# Main function
def main():
    # Create Facebook story with photo and music
    facebook_builder = FacebookConcreteBuilder()
    director = StoryDirector()
    director.construct(facebook_builder)
    director.music_story()
    facebook_story = facebook_builder.story
    print("\nFacebook Story:")
    facebook_story.show()
    
    # Create Instagram story with video and effects
    instagram_builder = InstagramConcreteBuilder()
    director = StoryDirector()
    director.construct(instagram_builder)
    director.video_story()
    instagram_story = instagram_builder.story
    print("\nInstagram Story:")
    instagram_story.show()

if __name__ == "__main__":
    main()