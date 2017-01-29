# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import binascii
import os

from django.db import models
from django.utils import timezone
from django.core.exceptions import ValidationError 

class TokensAbstract(models.Model):
    """
    Activation codes that an user can use to take ownership of a Connector
    """
    token = models.CharField(max_length=254, unique=True)
    creationDateTime = models.DateTimeField(auto_now_add=True)
    expirationDateTime = models.DateField(null=True, blank=True)
    
    def __str__(self):
        return self.token or 'no token'
    
    def clean(self):
        if self.expirationDateTime is not None:
            start = timezone.now()
            if self.creationDateTime is not None:
                start = self.creationDateTime
            
            if start > self.expirationDateTime:
                raise ValidationError({'expirationDateTime': ['Expirations date time must be greatest than creation date time']})
            
    def save(self, *args, **kwargs):
        self.clean()
        l = 10
        if not self.token:
            token = TokensAbstract.generateToken(l)
            for t in range(0, 230):
                token = TokensAbstract.generateToken(l)
                if self.tokenIsUnique(token):
                    break
                l += 1
            self.token = token
        return super(TokensAbstract, self).save(*args, **kwargs)
    
    def tokenIsUnique(self, token):
        currentPk = 0
        if self.pk is not None:
            currentPk = self.pk
        return self.__class__.objects.filter(token=token).exclude(pk=currentPk).count() == 0
    
    @staticmethod
    def generateToken(token_length=10):
        return binascii.hexlify(os.urandom(token_length)).decode()
    
    class Meta:
        abstract = True
        
