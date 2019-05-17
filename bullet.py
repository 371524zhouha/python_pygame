import pygame
from pygame.sprite import Sprite

class Bullet(Sprite):
    def __init__(self,ai_settings,screen,ship):
        super(Bullet,self).__init__()
        self.screen=screen

        self.rect=pygame.Rect(0,0,ai_settings.bullet_width,ai_settings.bullet_height)
        # self.rect=pygame.Rect(0,0,ai_settings.bullet_height,ai_settings.bullet_width)
        # self.rect.centery=ship.rect.centery
        # self.rect.left=ship.rect.right
        self.rect.centerx=ship.rect.centerx
        self.rect.top=ship.rect.top

        self.y=float(self.rect.y)
        # self.left = float(self.rect.left)

        self.color=ai_settings.bullet_color
        self.speed_factor=ai_settings.bullet_speed_factor

    # def update(self):
    #     # self.y-=self.speed_factor
    #     # self.rect.y=self.y
    #     # 更新表示子弹位置的小数值
    #     self.left += self.speed_factor
    #     # 更新表示子弹的rect的位置
    #     self.rect.left = self.left
    def update(self):
        """Move the bullet up the screen."""
        # Update the decimal position of the bullet.
        self.y -= self.speed_factor
        # Update the rect position.
        self.rect.y = self.y

    def draw_bullet(self):
        pygame.draw.rect(self.screen,self.color,self.rect)