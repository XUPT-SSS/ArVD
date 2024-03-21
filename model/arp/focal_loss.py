import torch
import torch.nn as nn
import torch.nn.functional as F

# def focal_loss(input,target,gamma=2,alpha=None,reduction='mean'):
#     ce_loss =F.cross_entropy(input,target,reduction='none')
#     pt=torch.exp(-ce_loss)
#     focal_loss = ((1-pt)**gamma)*ce_loss
#
#     if alpha is not None:
#         alpha_weight=torch.ones_like(target)*alpha
#         alpha_weight[target==1]=1-alpha
#         focal_loss=alpha_weight*focal_loss
#
#     if reduction == 'mean':
#         return focal_loss.mean()
#     elif reduction == 'sum':
#         return focal_loss.sum()
#     else:
#         return focal_loss

class FocalLoss(nn.Module):
    def __init__(self,alpha=1,gama=2):
        super(FocalLoss,self).__init__()
        self.alpha=alpha
        self.gama=gama

    # def forward(self,ce_loss,input,target,reduction):
    def forward(self, ce_loss, reduction):
        # ce_loss = F.cross_entropy(input, target)
        # ce_loss=nn.CrossEntropyLoss(input,target)
        pt = torch.exp(-ce_loss)
        focal_loss = self.alpha*(1-pt)**self.gama * ce_loss
        if reduction == 'mean':
            return focal_loss.mean()
        elif reduction == 'sum':
            return focal_loss.sum()
        else:
            return focal_loss


# self._loss = torch.nn.BCEWithLogitsLoss()
            # self._loss = FocalLoss(alpha=1,gama=5)
# loss1=torch.nn.CrossEntropyLoss()
# loss2 = loss1(logits,label.long().view(-1))
# loss = self._loss(loss2,'sum')