class cat:
    def speak(self):
        print("meow")
class dog:
    def speak(self):
        print("bark")
animal= [cat(),dog()]
for animals in animal:
            animals.speak()
# Polymorphism: Different classes with the same method name
        


class robort :
      def speak(self):
            print("metallic voice")
class human:
      def speak (self):
            print("human voice")
voices = [robort(),human()]
for voice in  voices:
      voice.speak()