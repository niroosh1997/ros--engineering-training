
import rclpy
from rclpy.node import Node
from turtlesim.msg import Pose

class TurtleController(Node):
    def __init__(self) -> None:
        super().__init__('TurtleController')
        self.get_logger().info("node initlized")
        self._turtle_publisher = self.create_publisher(Pose,"/turtle1/pose",10)
        self._timer = self.create_timer(0.1,self._timer_callback)
    
    def _timer_callback(self) -> None:
        output_pose = Pose()
        output_pose.x = 1.0
        output_pose.y = 2.0
        
        self._turtle_publisher.publish(output_pose)
        
        
        

def main(args=None):
    rclpy.init(args=args)

    turtle_controller = TurtleController()

    rclpy.spin(turtle_controller)

    # Destroy the node explicitly
    # (optional - otherwise it will be done automatically
    # when the garbage collector destroys the node object)
    turtle_controller.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()