
# When you override this class , you have 3 method implementations to fill in.
#
# ProcessInput - This method will receive all the events that happened since the last frame.
# Update - Put your game logic in here for the scene.
#     Render - Put     your     render     code     here.It     will     receive     the
#     main     screen     Surface as input.
#
# Of course, this class needs the appropriate harness to work.
# Here is an example program that does something simple: \
#     It launches the PyGame pipeline with a scene that is a blank red background.
# When you press the ENTER key, it changes to blue.
# This code may seem like overkill, but it does lots of other subtle things as well while at
#     the same time keeps the complexity of your game logic contained into a snazzy OO model.
#     Once you start adding more complexity to your game, this model will save you lots of headaches.
#     Additional benefits are listed below.
# # The first half is just boiler-plate stuff...


class SceneBase:
    def __init__(self):
        self.next = self

    def ProcessInput(self, events, pressed_keys):
        print("uh-oh, you didn't override this in the child class")

    def Update(self):
        print("uh-oh, you didn't override this in the child class")

    def Render(self, screen):
        print("uh-oh, you didn't override this in the child class")

    def SwitchToScene(self, next_scene):
        self.next = next_scene

    def Terminate(self):
        self.SwitchToScene(None)