
import numpy as np
import argparse

def gd(theta, lr=0.1, momentum=0.):
    grad = 4*theta**3 - 3*theta**2 - 10*theta
    theta = theta - lr*grad
    theta += momentum
    return theta


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--momentum',
                        default=False,
                        action='store_true',
                        help='use momentum')
    parser.add_argument('--schedule',
                        default=False,
                        action='store_true',
                        help='use learning rate schedule')
    parser.add_argument('--lr',
                        default=0.1,
                        type=float,
                        help='use learning rate schedule')
    args = parser.parse_args()
    theta_0 = -2
    lr = args.lr
    momentum = 0
    alpha = 0.1
    for i in range(20):
        if args.schedule:
            if i > 15:
                lr = 0.005
            elif i > 5:
                lr = 0.01
        
        theta_1 = gd(theta_0, lr=lr, momentum=alpha*momentum)
        print("%0.2f, %0.2f" % (theta_0, theta_1))

        if args.momentum:
            momentum = theta_1 - theta_0 

        theta_0 = theta_1

