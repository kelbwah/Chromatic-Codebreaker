import import_handler as shared
import buttons_and_text, circles, game_logic
class GameScreen:
    def __init__(self):
        self.next_screen = None
        self.screen_done = False
        self.screen = shared.screen
        self.game_logic = game_logic.Sequence()
        self.sequence = None
        self.curr_guess = None
        self.buttons_and_text = buttons_and_text.ButtonsAndText()
        self.guess_outcome = None

        self.image_counters = [0 for i in range(6)]

        self.sprite_group_1 = shared.pygame.sprite.Group()
        for image in shared.images:
            self.sprite_group_1.add(circles.Circle(image, 0))
        self.sprite_group_1 = list(self.sprite_group_1)

        self.sprite_group_2 = shared.pygame.sprite.Group()
        for image in shared.images:
            self.sprite_group_2.add(circles.Circle(image, 1))
        self.sprite_group_2 = list(self.sprite_group_2)

        self.sprite_group_3 = shared.pygame.sprite.Group()
        for image in shared.images:
            self.sprite_group_3.add(circles.Circle(image, 2))
        self.sprite_group_3 = list(self.sprite_group_3)

        self.sprite_group_4 = shared.pygame.sprite.Group()
        for image in shared.images:
            self.sprite_group_4.add(circles.Circle(image, 3))
        self.sprite_group_4 = list(self.sprite_group_4)

        self.sprite_group_5 = shared.pygame.sprite.Group()
        for image in shared.images:
            self.sprite_group_5.add(circles.Circle(image, 4))
        self.sprite_group_5 = list(self.sprite_group_5)

        self.sprite_group_6 = shared.pygame.sprite.Group()
        for image in shared.images:
            self.sprite_group_6.add(circles.Circle(image, 5))
        self.sprite_group_6 = list(self.sprite_group_6)

        self.add_arrows()
        self.add_shrinked_arrows()

        self.up_arrow1_pressed = False
        self.up_arrow2_pressed = False
        self.up_arrow3_pressed = False
        self.up_arrow4_pressed = False
        self.up_arrow5_pressed = False
        self.up_arrow6_pressed = False

        self.down_arrow1_pressed = False
        self.down_arrow2_pressed = False
        self.down_arrow3_pressed = False
        self.down_arrow4_pressed = False
        self.down_arrow5_pressed = False
        self.down_arrow6_pressed = False

        self.guess_button_pressed = False
        self.sequence_button_pressed = False
        self.retry_button_pressed = False

        self.best_score = 0
        self.curr_score = 0

        self.first_try = True

        self.play_music_button_clicked = False
        self.pause_music_button_clicked = False
        self.return_button_pressed = False

    def create_curr_guess(self):
        self.guess = []
        for color in self.image_counters:
            self.guess.append(shared.color_dictionary[color])
        return self.guess

    def get_mouse_pos(self):
        return shared.pygame.mouse.get_pos()


    def handle_event(self, event):
        # Handle any user input, such as button clicks
        if event.type == shared.pygame.QUIT:
            shared.sys.exit()
        elif event.type == shared.pygame.MOUSEBUTTONDOWN:
            if self.get_mouse_pos()[0] > self.up_arrow1[1].left and self.get_mouse_pos()[0] < self.up_arrow1[1].right and self.get_mouse_pos()[1] > self.up_arrow1[1].top and self.get_mouse_pos()[1] < self.up_arrow1[1].bottom:
                self.up_arrow1_pressed = True
            elif self.get_mouse_pos()[0] > self.up_arrow2[1].left and self.get_mouse_pos()[0] < self.up_arrow2[1].right and self.get_mouse_pos()[1] > self.up_arrow2[1].top and self.get_mouse_pos()[1] < self.up_arrow2[1].bottom:
                self.up_arrow2_pressed = True
            elif self.get_mouse_pos()[0] > self.up_arrow3[1].left and self.get_mouse_pos()[0] < self.up_arrow3[1].right and self.get_mouse_pos()[1] > self.up_arrow3[1].top and self.get_mouse_pos()[1] < self.up_arrow3[1].bottom:
                self.up_arrow3_pressed = True
            elif self.get_mouse_pos()[0] > self.up_arrow4[1].left and self.get_mouse_pos()[0] < self.up_arrow4[1].right and self.get_mouse_pos()[1] > self.up_arrow4[1].top and self.get_mouse_pos()[1] < self.up_arrow4[1].bottom:
                self.up_arrow4_pressed = True
            elif self.get_mouse_pos()[0] > self.up_arrow5[1].left and self.get_mouse_pos()[0] < self.up_arrow5[1].right and self.get_mouse_pos()[1] > self.up_arrow5[1].top and self.get_mouse_pos()[1] < self.up_arrow5[1].bottom:
                self.up_arrow5_pressed = True
            elif self.get_mouse_pos()[0] > self.up_arrow6[1].left and self.get_mouse_pos()[0] < self.up_arrow6[1].right and self.get_mouse_pos()[1] > self.up_arrow6[1].top and self.get_mouse_pos()[1] < self.up_arrow6[1].bottom:
                self.up_arrow6_pressed = True
            elif self.get_mouse_pos()[0] > self.down_arrow1[1].left and self.get_mouse_pos()[0] < self.down_arrow1[1].right and self.get_mouse_pos()[1] > self.down_arrow1[1].top and self.get_mouse_pos()[1] < self.down_arrow1[1].bottom:
                self.down_arrow1_pressed = True
            elif self.get_mouse_pos()[0] > self.down_arrow2[1].left and self.get_mouse_pos()[0] < self.down_arrow2[1].right and self.get_mouse_pos()[1] > self.down_arrow2[1].top and self.get_mouse_pos()[1] < self.down_arrow2[1].bottom:
                self.down_arrow2_pressed = True
            elif self.get_mouse_pos()[0] > self.down_arrow3[1].left and self.get_mouse_pos()[0] < self.down_arrow3[1].right and self.get_mouse_pos()[1] > self.down_arrow3[1].top and self.get_mouse_pos()[1] < self.down_arrow3[1].bottom:
                self.down_arrow3_pressed = True
            elif self.get_mouse_pos()[0] > self.down_arrow4[1].left and self.get_mouse_pos()[0] < self.down_arrow4[1].right and self.get_mouse_pos()[1] > self.down_arrow4[1].top and self.get_mouse_pos()[1] < self.down_arrow4[1].bottom:
                self.down_arrow4_pressed = True
            elif self.get_mouse_pos()[0] > self.down_arrow5[1].left and self.get_mouse_pos()[0] < self.down_arrow5[1].right and self.get_mouse_pos()[1] > self.down_arrow5[1].top and self.get_mouse_pos()[1] < self.down_arrow5[1].bottom:
                self.down_arrow5_pressed = True
            elif self.get_mouse_pos()[0] > self.down_arrow6[1].left and self.get_mouse_pos()[0] < self.down_arrow6[1].right and self.get_mouse_pos()[1] > self.down_arrow6[1].top and self.get_mouse_pos()[1] < self.down_arrow6[1].bottom:
                self.down_arrow6_pressed = True
            elif self.get_mouse_pos()[0] > self.buttons_and_text.guess_button.left and self.get_mouse_pos()[0] < self.buttons_and_text.guess_button.right and self.get_mouse_pos()[1] > self.buttons_and_text.guess_button.top and self.get_mouse_pos()[1] < self.buttons_and_text.guess_button.bottom:
                self.guess_button_pressed = True
            elif self.get_mouse_pos()[0] > self.buttons_and_text.sequence_button.left and self.get_mouse_pos()[0] < self.buttons_and_text.sequence_button.right and self.get_mouse_pos()[1] > self.buttons_and_text.sequence_button.top and self.get_mouse_pos()[1] < self.buttons_and_text.sequence_button.bottom:
                self.sequence_button_pressed = True
            elif self.guess_outcome == 'You got the correct sequence!' and self.get_mouse_pos()[0] > self.buttons_and_text.retry_button.left and self.get_mouse_pos()[0] < self.buttons_and_text.retry_button.right and self.get_mouse_pos()[1] > self.buttons_and_text.retry_button.top and self.get_mouse_pos()[1] < self.buttons_and_text.retry_button.bottom:
                self.retry_button_pressed = True
            elif shared.music_paused == False and self.get_mouse_pos()[0] > self.buttons_and_text.pause_music_button_rect.left and self.get_mouse_pos()[0] < self.buttons_and_text.pause_music_button_rect.right and self.get_mouse_pos()[1] > self.buttons_and_text.pause_music_button_rect.top and self.get_mouse_pos()[1] < self.buttons_and_text.pause_music_button_rect.bottom:
                self.pause_music_button_clicked = True
            elif shared.music_paused == True and self.get_mouse_pos()[0] > self.buttons_and_text.play_music_button_rect.left and self.get_mouse_pos()[0] < self.buttons_and_text.play_music_button_rect.right and self.get_mouse_pos()[1] > self.buttons_and_text.play_music_button_rect.top and self.get_mouse_pos()[1] < self.buttons_and_text.play_music_button_rect.bottom:
                self.play_music_button_clicked = True     
            elif self.get_mouse_pos()[0] > self.buttons_and_text.return_button.left and self.get_mouse_pos()[0] < self.buttons_and_text.return_button.right and self.get_mouse_pos()[1] < self.buttons_and_text.return_button.bottom and self.get_mouse_pos()[1] > self.buttons_and_text.return_button.top:
                self.return_button_pressed = True 
        ##################################################################################################################
        ##################################################################################################################
        elif event.type == shared.pygame.MOUSEBUTTONUP:
            if self.get_mouse_pos()[0] > self.up_arrow1[1].left and self.get_mouse_pos()[0] < self.up_arrow1[1].right and self.get_mouse_pos()[1] > self.up_arrow1[1].top and self.get_mouse_pos()[1] < self.up_arrow1[1].bottom:
                if self.image_counters[0] == 8:
                    self.image_counters[0] = 0
                else:
                    self.image_counters[0]+=1
                self.up_arrow1_pressed = False
            elif self.get_mouse_pos()[0] > self.up_arrow2[1].left and self.get_mouse_pos()[0] < self.up_arrow2[1].right and self.get_mouse_pos()[1] > self.up_arrow2[1].top and self.get_mouse_pos()[1] < self.up_arrow2[1].bottom:
                if self.image_counters[1] == 8:
                    self.image_counters[1] = 0
                else:
                    self.image_counters[1]+=1
                self.up_arrow2_pressed = False
            elif self.get_mouse_pos()[0] > self.up_arrow3[1].left and self.get_mouse_pos()[0] < self.up_arrow3[1].right and self.get_mouse_pos()[1] > self.up_arrow3[1].top and self.get_mouse_pos()[1] < self.up_arrow3[1].bottom:
                if self.image_counters[2] == 8:
                    self.image_counters[2] = 0
                else:
                    self.image_counters[2]+=1
                self.up_arrow3_pressed = False
            elif self.get_mouse_pos()[0] > self.up_arrow4[1].left and self.get_mouse_pos()[0] < self.up_arrow4[1].right and self.get_mouse_pos()[1] > self.up_arrow4[1].top and self.get_mouse_pos()[1] < self.up_arrow4[1].bottom:
                if self.image_counters[3] == 8:
                    self.image_counters[3] = 0
                else:
                    self.image_counters[3]+=1
                self.up_arrow4_pressed = False
            elif self.get_mouse_pos()[0] > self.up_arrow5[1].left and self.get_mouse_pos()[0] < self.up_arrow5[1].right and self.get_mouse_pos()[1] > self.up_arrow5[1].top and self.get_mouse_pos()[1] < self.up_arrow5[1].bottom:
                if self.image_counters[4] == 8:
                    self.image_counters[4] = 0
                else:
                    self.image_counters[4]+=1
                self.up_arrow5_pressed = False
            elif self.get_mouse_pos()[0] > self.up_arrow6[1].left and self.get_mouse_pos()[0] < self.up_arrow6[1].right and self.get_mouse_pos()[1] > self.up_arrow6[1].top and self.get_mouse_pos()[1] < self.up_arrow6[1].bottom:
                if self.image_counters[5] == 8:
                    self.image_counters[5] = 0
                else:
                    self.image_counters[5]+=1
                self.up_arrow6_pressed = False
            elif self.get_mouse_pos()[0] > self.down_arrow1[1].left and self.get_mouse_pos()[0] < self.down_arrow1[1].right and self.get_mouse_pos()[1] > self.down_arrow1[1].top and self.get_mouse_pos()[1] < self.down_arrow1[1].bottom:
                if self.image_counters[0] == 0:
                    self.image_counters[0] = 8
                else:
                    self.image_counters[0]-=1
                self.down_arrow1_pressed = False
            elif self.get_mouse_pos()[0] > self.down_arrow2[1].left and self.get_mouse_pos()[0] < self.down_arrow2[1].right and self.get_mouse_pos()[1] > self.down_arrow2[1].top and self.get_mouse_pos()[1] < self.down_arrow2[1].bottom:
                if self.image_counters[1] == 0:
                    self.image_counters[1] = 8
                else:
                    self.image_counters[1]-=1
                self.down_arrow2_pressed = False
            elif self.get_mouse_pos()[0] > self.down_arrow3[1].left and self.get_mouse_pos()[0] < self.down_arrow3[1].right and self.get_mouse_pos()[1] > self.down_arrow3[1].top and self.get_mouse_pos()[1] < self.down_arrow3[1].bottom:
                if self.image_counters[2] == 0:
                    self.image_counters[2] = 8
                else:
                    self.image_counters[2]-=1
                self.down_arrow3_pressed = False
            elif self.get_mouse_pos()[0] > self.down_arrow4[1].left and self.get_mouse_pos()[0] < self.down_arrow4[1].right and self.get_mouse_pos()[1] > self.down_arrow4[1].top and self.get_mouse_pos()[1] < self.down_arrow4[1].bottom:
                if self.image_counters[3] == 0:
                    self.image_counters[3] = 8
                else:
                    self.image_counters[3]-=1
                self.down_arrow4_pressed = False
            elif self.get_mouse_pos()[0] > self.down_arrow5[1].left and self.get_mouse_pos()[0] < self.down_arrow5[1].right and self.get_mouse_pos()[1] > self.down_arrow5[1].top and self.get_mouse_pos()[1] < self.down_arrow5[1].bottom:
                if self.image_counters[4] == 0:
                    self.image_counters[4] = 8
                else:
                    self.image_counters[4]-=1
                self.down_arrow5_pressed = False
            elif self.get_mouse_pos()[0] > self.down_arrow6[1].left and self.get_mouse_pos()[0] < self.down_arrow6[1].right and self.get_mouse_pos()[1] > self.down_arrow6[1].top and self.get_mouse_pos()[1] < self.down_arrow6[1].bottom:
                if self.image_counters[5] == 0:
                    self.image_counters[5] = 8
                else:
                    self.image_counters[5]-=1
                self.down_arrow6_pressed = False
            elif self.get_mouse_pos()[0] > self.buttons_and_text.guess_button.left and self.get_mouse_pos()[0] < self.buttons_and_text.guess_button.right and self.get_mouse_pos()[1] > self.buttons_and_text.guess_button.top and self.get_mouse_pos()[1] < self.buttons_and_text.guess_button.bottom:
                if self.sequence != None:
                    self.game_logic.guess = self.create_curr_guess()
                    self.guess_outcome = self.game_logic.guess_sequence()
                    if self.guess_outcome != 'You got the correct sequence!':
                        self.guess_outcome = list(self.game_logic.guess_sequence().values())
                    print(self.guess_outcome, self.game_logic.sequence)
                    self.curr_score += 1
                self.guess_button_pressed = False
            elif self.get_mouse_pos()[0] > self.buttons_and_text.sequence_button.left and self.get_mouse_pos()[0] < self.buttons_and_text.sequence_button.right and self.get_mouse_pos()[1] > self.buttons_and_text.sequence_button.top and self.get_mouse_pos()[1] < self.buttons_and_text.sequence_button.bottom:
                self.sequence = self.game_logic.create_random_sequence()
                if self.guess_outcome != None:
                    self.guess_outcome = None
                self.image_counters = [0 for i in range(6)]
                self.curr_guess = None
                self.curr_score = 0
                self.sequence_button_pressed = False
            elif self.guess_outcome == 'You got the correct sequence!' and self.get_mouse_pos()[0] > self.buttons_and_text.retry_button.left and self.get_mouse_pos()[0] < self.buttons_and_text.retry_button.right and self.get_mouse_pos()[1] > self.buttons_and_text.retry_button.top and self.get_mouse_pos()[1] < self.buttons_and_text.retry_button.bottom:
                self.guess_outcome = None
                self.curr_guess = None
                self.game_logic = game_logic.Sequence()
                self.sequence = None
                self.image_counters = [0 for i in range(6)]
                if self.first_try == True:
                    self.best_score = self.curr_score
                    self.first_try = False
                elif self.first_try == False:
                    if self.curr_score < self.best_score:
                        self.best_score = self.curr_score
                self.curr_score = 0
                self.retry_button_pressed = False
            elif shared.music_paused == False and self.get_mouse_pos()[0] > self.buttons_and_text.pause_music_button_rect.left and self.get_mouse_pos()[0] < self.buttons_and_text.pause_music_button_rect.right and self.get_mouse_pos()[1] > self.buttons_and_text.pause_music_button_rect.top and self.get_mouse_pos()[1] < self.buttons_and_text.pause_music_button_rect.bottom:
                shared.music_paused = True
                shared.pygame.mixer.music.pause()
                self.pause_music_button_clicked = False
            elif shared.music_paused == True and self.get_mouse_pos()[0] > self.buttons_and_text.play_music_button_rect.left and self.get_mouse_pos()[0] < self.buttons_and_text.play_music_button_rect.right and self.get_mouse_pos()[1] > self.buttons_and_text.play_music_button_rect.top and self.get_mouse_pos()[1] < self.buttons_and_text.play_music_button_rect.bottom:
                shared.pygame.mixer.music.play(-1)
                shared.music_paused = False
                self.play_music_button_clicked = False   
            elif self.get_mouse_pos()[0] > self.buttons_and_text.return_button.left and self.get_mouse_pos()[0] < self.buttons_and_text.return_button.right and self.get_mouse_pos()[1] < self.buttons_and_text.return_button.bottom and self.get_mouse_pos()[1] > self.buttons_and_text.return_button.top:
                self.return_button_pressed = False
                self.screen_done = True
                self.next_screen = 'home_screen'

            self.up_arrow1_pressed = False
            self.up_arrow2_pressed = False
            self.up_arrow3_pressed = False
            self.up_arrow4_pressed = False
            self.up_arrow5_pressed = False
            self.up_arrow6_pressed = False

            self.down_arrow1_pressed = False
            self.down_arrow2_pressed = False
            self.down_arrow3_pressed = False
            self.down_arrow4_pressed = False
            self.down_arrow5_pressed = False
            self.down_arrow6_pressed = False

            self.guess_button_pressed = False
            self.sequence_button_pressed = False
            self.retry_button_pressed = False

            self.play_music_button_clicked = False
            self.pause_music_button_clicked = False
            self.return_button_pressed = False
    
    def add_arrows(self):
        self.up_arrow1 = self.buttons_and_text.create_up_arrow_button(shared.screen_width/7, shared.screen_height/3)
        self.up_arrow2 = self.buttons_and_text.create_up_arrow_button(shared.screen_width/3.4, shared.screen_height/3)
        self.up_arrow3 = self.buttons_and_text.create_up_arrow_button(shared.screen_width/2.3, shared.screen_height/3)
        self.up_arrow4 = self.buttons_and_text.create_up_arrow_button(shared.screen_width/1.73, shared.screen_height/3)
        self.up_arrow5 = self.buttons_and_text.create_up_arrow_button(shared.screen_width/1.4, shared.screen_height/3)
        self.up_arrow6 = self.buttons_and_text.create_up_arrow_button(shared.screen_width * 6 / 7, shared.screen_height/3)

        self.down_arrow1 = self.buttons_and_text.create_down_arrow_button(shared.screen_width/7 + 5, shared.screen_height/1.55)
        self.down_arrow2 = self.buttons_and_text.create_down_arrow_button(shared.screen_width/3.4 + 5, shared.screen_height/1.55)
        self.down_arrow3 = self.buttons_and_text.create_down_arrow_button(shared.screen_width/2.3 + 5, shared.screen_height/1.55)
        self.down_arrow4 = self.buttons_and_text.create_down_arrow_button(shared.screen_width/1.73 + 5, shared.screen_height/1.55)
        self.down_arrow5 = self.buttons_and_text.create_down_arrow_button(shared.screen_width/1.4 + 5, shared.screen_height/1.55)
        self.down_arrow6 = self.buttons_and_text.create_down_arrow_button(shared.screen_width * 6 / 7 + 5, shared.screen_height/1.55)

    def add_shrinked_arrows(self):
        self.shrinked_up_arrow1 = self.buttons_and_text.create_shrinked_up_arrow_button(shared.screen_width/7, shared.screen_height/3)
        self.shrinked_up_arrow2 = self.buttons_and_text.create_shrinked_up_arrow_button(shared.screen_width/3.4, shared.screen_height/3)
        self.shrinked_up_arrow3 = self.buttons_and_text.create_shrinked_up_arrow_button(shared.screen_width/2.3, shared.screen_height/3)
        self.shrinked_up_arrow4 = self.buttons_and_text.create_shrinked_up_arrow_button(shared.screen_width/1.73, shared.screen_height/3)
        self.shrinked_up_arrow5 = self.buttons_and_text.create_shrinked_up_arrow_button(shared.screen_width/1.4, shared.screen_height/3)
        self.shrinked_up_arrow6 = self.buttons_and_text.create_shrinked_up_arrow_button(shared.screen_width * 6 / 7, shared.screen_height/3)

        self.shrinked_down_arrow1 = self.buttons_and_text.create_shrinked_down_arrow_button(shared.screen_width/7 + 5, shared.screen_height/1.55)
        self.shrinked_down_arrow2 = self.buttons_and_text.create_shrinked_down_arrow_button(shared.screen_width/3.4 + 5, shared.screen_height/1.55)
        self.shrinked_down_arrow3 = self.buttons_and_text.create_shrinked_down_arrow_button(shared.screen_width/2.3 + 5, shared.screen_height/1.55)
        self.shrinked_down_arrow4 = self.buttons_and_text.create_shrinked_down_arrow_button(shared.screen_width/1.73 + 5, shared.screen_height/1.55)
        self.shrinked_down_arrow5 = self.buttons_and_text.create_shrinked_down_arrow_button(shared.screen_width/1.4 + 5, shared.screen_height/1.55)
        self.shrinked_down_arrow6 = self.buttons_and_text.create_shrinked_down_arrow_button(shared.screen_width * 6 / 7 + 5, shared.screen_height/1.55)

    def draw_arrows(self):
        if self.up_arrow1_pressed == False:
            self.screen.blit(self.up_arrow1[0], self.up_arrow1[1])
        else:
            self.screen.blit(self.shrinked_up_arrow1[0], self.shrinked_up_arrow1[1])

        if self.up_arrow2_pressed == False:
            self.screen.blit(self.up_arrow2[0], self.up_arrow2[1])
        else:
            self.screen.blit(self.shrinked_up_arrow2[0], self.shrinked_up_arrow2[1])

        if self.up_arrow3_pressed == False:
            self.screen.blit(self.up_arrow3[0], self.up_arrow3[1])
        else:
            self.screen.blit(self.shrinked_up_arrow3[0], self.shrinked_up_arrow3[1])

        if self.up_arrow4_pressed == False:
            self.screen.blit(self.up_arrow4[0], self.up_arrow4[1])
        else:
            self.screen.blit(self.shrinked_up_arrow4[0], self.shrinked_up_arrow4[1])

        if self.up_arrow5_pressed == False:
            self.screen.blit(self.up_arrow5[0], self.up_arrow5[1])
        else:
            self.screen.blit(self.shrinked_up_arrow5[0], self.shrinked_up_arrow5[1])

        if self.up_arrow6_pressed == False:
            self.screen.blit(self.up_arrow6[0], self.up_arrow6[1])
        else:
            self.screen.blit(self.shrinked_up_arrow6[0], self.shrinked_up_arrow6[1])

        if self.down_arrow1_pressed == False:
            self.screen.blit(self.down_arrow1[0], self.down_arrow1[1])
        else:
            self.screen.blit(self.shrinked_down_arrow1[0], self.shrinked_down_arrow1[1])

        if self.down_arrow2_pressed == False:
            self.screen.blit(self.down_arrow2[0], self.down_arrow2[1])
        else:
            self.screen.blit(self.shrinked_down_arrow2[0], self.shrinked_down_arrow2[1])

        if self.down_arrow3_pressed == False:
            self.screen.blit(self.down_arrow3[0], self.down_arrow3[1])
        else:
            self.screen.blit(self.shrinked_down_arrow3[0], self.shrinked_down_arrow3[1])

        if self.down_arrow4_pressed == False:
            self.screen.blit(self.down_arrow4[0], self.down_arrow4[1])
        else:
            self.screen.blit(self.shrinked_down_arrow4[0], self.shrinked_down_arrow4[1])

        if self.down_arrow5_pressed == False:
            self.screen.blit(self.down_arrow5[0], self.down_arrow5[1])
        else:
            self.screen.blit(self.shrinked_down_arrow5[0], self.shrinked_down_arrow5[1])

        if self.down_arrow6_pressed == False:
            self.screen.blit(self.down_arrow6[0], self.down_arrow6[1])
        else:
            self.screen.blit(self.shrinked_down_arrow6[0], self.shrinked_down_arrow6[1])


    def draw(self):
        self.screen.fill(shared.light_blue)

        if (self.guess_outcome != None and self.guess_outcome != 'You got the correct sequence!') or self.guess_outcome == None:
            self.draw_arrows()
        
        if self.sequence_button_pressed == False and ((self.guess_outcome != None and self.guess_outcome != 'You got the correct sequence!') or self.guess_outcome == None):
            self.buttons_and_text.create_sequence_button()
        elif self.sequence_button_pressed == True and ((self.guess_outcome != None and self.guess_outcome != 'You got the correct sequence!') or self.guess_outcome == None):
            self.buttons_and_text.shrink_sequence_button()

        if (self.guess_outcome != None and self.guess_outcome != 'You got the correct sequence!') or self.guess_outcome == None:
            self.sprite_group_1[self.image_counters[0]].draw()
            self.sprite_group_2[self.image_counters[1]].draw()
            self.sprite_group_3[self.image_counters[2]].draw()
            self.sprite_group_4[self.image_counters[3]].draw()
            self.sprite_group_5[self.image_counters[4]].draw()
            self.sprite_group_6[self.image_counters[5]].draw()

        if self.sequence == None and ((self.guess_outcome != None and self.guess_outcome != 'You got the correct sequence!') or self.guess_outcome == None):
            self.buttons_and_text.create_no_sequence_text()
        elif self.sequence != None and ((self.guess_outcome != None and self.guess_outcome != 'You got the correct sequence!') or self.guess_outcome == None):
            self.buttons_and_text.create_has_sequence_text()
            
        if self.guess_button_pressed == False and ((self.guess_outcome != None and self.guess_outcome != 'You got the correct sequence!') or self.guess_outcome == None):
            self.buttons_and_text.create_guess_button()
        elif self.guess_button_pressed == True and ((self.guess_outcome != None and self.guess_outcome != 'You got the correct sequence!') or self.guess_outcome == None):
            self.buttons_and_text.shrink_guess_button()

        if self.guess_outcome != None and self.guess_outcome != 'You got the correct sequence!':
            self.buttons_and_text.create_hints_text(self.guess_outcome)
        elif self.guess_outcome != None and self.guess_outcome == 'You got the correct sequence!':
            self.buttons_and_text.create_win_text()
            if self.retry_button_pressed == False:
                self.buttons_and_text.create_retry_button()
            else:
                self.buttons_and_text.shrink_retry_button()
        
        self.buttons_and_text.create_score_text(self.curr_score, self.best_score)

        if self.play_music_button_clicked == True and shared.music_paused == True:
            self.buttons_and_text.shrink_music_play_button()
        elif self.play_music_button_clicked == False and shared.music_paused == True:
            self.buttons_and_text.create_music_play_button()
        elif self.pause_music_button_clicked == True and shared.music_paused == False:
            self.buttons_and_text.shrink_music_pause_button()
        elif self.pause_music_button_clicked == False and shared.music_paused == False:
            self.buttons_and_text.create_music_pause_button()

        if self.return_button_pressed == True:
            self.buttons_and_text.shrink_return_button(2)
        else:
            self.buttons_and_text.create_return_button(2)

    def update(self):
        pass

    def is_done(self):
        if self.screen_done == True:
            return True
        elif self.screen_done == False:
            return False