
import torch, torch.nn as nn
from torch.utils.data import DataLoader
# TODO: implementar Dataset multimodal
class FusionNet(nn.Module):
    def __init__(self, n_classes=100):
        super().__init__()
        self.img_backbone = nn.Sequential(nn.Conv2d(3,16,3,1,1), nn.ReLU(), nn.AdaptiveAvgPool2d((1,1)))
        self.rf_backbone  = nn.Sequential(nn.Conv2d(1,16,3,1,1), nn.ReLU(), nn.AdaptiveAvgPool2d((1,1)))
        self.au_backbone  = nn.Sequential(nn.Conv2d(1,16,3,1,1), nn.ReLU(), nn.AdaptiveAvgPool2d((1,1)))
        self.fusion = nn.Sequential(nn.Flatten(), nn.Linear(48,128), nn.ReLU(), nn.Linear(128,n_classes))
    def forward(self, img, rf, aud):
        x1 = self.img_backbone(img)
        x2 = self.rf_backbone(rf)
        x3 = self.au_backbone(aud)
        x = torch.cat([x1,x2,x3], dim=1)
        return self.fusion(x)
if __name__ == '__main__':
    # TODO: loader = DataLoader(...)
    pass
