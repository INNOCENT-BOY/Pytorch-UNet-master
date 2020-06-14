import torch


from unet import UNet1 as UNet



dummy_input = torch.randn(1, 3, 304, 406)

# net = UNet(n_channels=3, depth=5, n_classes=21)
model = UNet(n_classes=21, in_channels=3, padding=True, up_mode='upsample')

out = model(dummy_input)
print(dummy_input.size())

# model.eval()
# # out = net(dummy_input)
#
# with torch.no_grad():
#     torch.onnx.export(model,
#                       dummy_input,
#                       'test.onnx',
#                       verbose=True)
#
