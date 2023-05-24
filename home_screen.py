import import_handler as shared
import buttons_and_text

class HomeScreen:
    def __init__(self):
        self.next_screen = None
        self.screen_done = False
        self.screen = shared.screen
        self.buttons_and_text = buttons_and_text.ButtonsAndText()
        self.play_button_clicked = False
        self.how_to_play_button_clicked = False
        self.exit_button_clicked = False
        self.play_music_button_clicked = False
        self.pause_music_button_clicked = False
        self.return_button_clicked = False

    def draw(self):
        self.screen.fill(shared.light_blue)
        self.buttons_and_text.create_title_text()

        if self.play_button_clicked == True:
            self.buttons_and_text.shrink_play_button()
        else:
            self.buttons_and_text.create_play_button()
        
        if self.how_to_play_button_clicked == True:
            self.buttons_and_text.shrink_how_to_play_button()
        else:
            self.buttons_and_text.create_how_to_play_button()
        
        if self.exit_button_clicked == True:
            self.buttons_and_text.shrink_exit_button()
        else:
            self.buttons_and_text.create_exit_button()

        if self.play_music_button_clicked == True and shared.music_paused == True:
            self.buttons_and_text.shrink_music_play_button()
        elif self.play_music_button_clicked == False and shared.music_paused == True:
            self.buttons_and_text.create_music_play_button()
        elif self.pause_music_button_clicked == True and shared.music_paused == False:
            self.buttons_and_text.shrink_music_pause_button()
        elif self.pause_music_button_clicked == False and shared.music_paused == False:
            self.buttons_and_text.create_music_pause_button()
        
        


    def update(self):
        pass

    def get_mouse_pos(self):
        return shared.pygame.mouse.get_pos()


    def handle_event(self, event):
        # Handle any user input, such as button clicks
        if event.type == shared.pygame.QUIT:
            shared.sys.exit()
        elif event.type == shared.pygame.MOUSEBUTTONDOWN:
            if self.get_mouse_pos()[0] > self.buttons_and_text.play_button.left and self.get_mouse_pos()[0] < self.buttons_and_text.play_button.right and self.get_mouse_pos()[1] > self.buttons_and_text.play_button.top and self.get_mouse_pos()[1] < self.buttons_and_text.play_button.bottom:
                self.play_button_clicked = True
            elif self.get_mouse_pos()[0] > self.buttons_and_text.how_to_play_button.left and self.get_mouse_pos()[0] < self.buttons_and_text.how_to_play_button.right and self.get_mouse_pos()[1] > self.buttons_and_text.how_to_play_button.top and self.get_mouse_pos()[1] < self.buttons_and_text.how_to_play_button.bottom:
                self.how_to_play_button_clicked = True
            elif self.get_mouse_pos()[0] > self.buttons_and_text.exit_button.left and self.get_mouse_pos()[0] < self.buttons_and_text.exit_button.right and self.get_mouse_pos()[1] > self.buttons_and_text.exit_button.top and self.get_mouse_pos()[1] < self.buttons_and_text.exit_button.bottom:
                self.exit_button_clicked = True
            elif shared.music_paused == False and self.get_mouse_pos()[0] > self.buttons_and_text.pause_music_button_rect.left and self.get_mouse_pos()[0] < self.buttons_and_text.pause_music_button_rect.right and self.get_mouse_pos()[1] > self.buttons_and_text.pause_music_button_rect.top and self.get_mouse_pos()[1] < self.buttons_and_text.pause_music_button_rect.bottom:
                self.pause_music_button_clicked = True
            elif shared.music_paused == True and self.get_mouse_pos()[0] > self.buttons_and_text.play_music_button_rect.left and self.get_mouse_pos()[0] < self.buttons_and_text.play_music_button_rect.right and self.get_mouse_pos()[1] > self.buttons_and_text.play_music_button_rect.top and self.get_mouse_pos()[1] < self.buttons_and_text.play_music_button_rect.bottom:
                self.play_music_button_clicked = True     
        elif event.type == shared.pygame.MOUSEBUTTONUP:
            if self.get_mouse_pos()[0] > self.buttons_and_text.play_button.left and self.get_mouse_pos()[0] < self.buttons_and_text.play_button.right and self.get_mouse_pos()[1] > self.buttons_and_text.play_button.top and self.get_mouse_pos()[1] < self.buttons_and_text.play_button.bottom:
                self.screen_done = True
                self.next_screen = 'game_screen'
                self.play_button_clicked = False
            elif self.get_mouse_pos()[0] > self.buttons_and_text.how_to_play_button.left and self.get_mouse_pos()[0] < self.buttons_and_text.how_to_play_button.right and self.get_mouse_pos()[1] > self.buttons_and_text.how_to_play_button.top and self.get_mouse_pos()[1] < self.buttons_and_text.how_to_play_button.bottom:
                self.screen_done = True
                self.next_screen = 'how_to_play_screen'
                self.how_to_play_button_clicked = False
            elif shared.music_paused == False and self.get_mouse_pos()[0] > self.buttons_and_text.pause_music_button_rect.left and self.get_mouse_pos()[0] < self.buttons_and_text.pause_music_button_rect.right and self.get_mouse_pos()[1] > self.buttons_and_text.pause_music_button_rect.top and self.get_mouse_pos()[1] < self.buttons_and_text.pause_music_button_rect.bottom:
                shared.music_paused = True
                shared.pygame.mixer.music.pause()
                self.pause_music_button_clicked = False
            elif shared.music_paused == True and self.get_mouse_pos()[0] > self.buttons_and_text.play_music_button_rect.left and self.get_mouse_pos()[0] < self.buttons_and_text.play_music_button_rect.right and self.get_mouse_pos()[1] > self.buttons_and_text.play_music_button_rect.top and self.get_mouse_pos()[1] < self.buttons_and_text.play_music_button_rect.bottom:
                shared.pygame.mixer.music.play(-1)
                shared.music_paused = False
                self.play_music_button_clicked = False   
            elif self.get_mouse_pos()[0] > self.buttons_and_text.exit_button.left and self.get_mouse_pos()[0] < self.buttons_and_text.exit_button.right and self.get_mouse_pos()[1] > self.buttons_and_text.exit_button.top and self.get_mouse_pos()[1] < self.buttons_and_text.exit_button.bottom: 
                self.exit_button_clicked = False
                shared.sys.exit()    

            self.play_button_clicked = False 
            self.how_to_play_button_clicked = False
            self.exit_button_clicked = False
            self.play_music_button_clicked = False
            self.pause_music_button_clicked = False
            self.return_button_clicked = False

    def is_done(self):
        if self.screen_done == True:
            return True
        elif self.screen_done == False:
            return False