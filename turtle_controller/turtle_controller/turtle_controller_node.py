
import rclpy
from rclpy.node import Node

class TurtleController(Node):
    def __init__(self) -> None:
        super().__init__('TurtleController')
        # self.publisher = self.create_publisher(String, 'topic', 10)
        
        
        

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