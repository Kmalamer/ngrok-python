# See API documentation for full information on the available functions:
# https://ngrok.github.io/ngrok-python/

def connect(
    addr: Union[None, str, int] = None,
    tunnel: Optional[NgrokTunnel] = None,
    **options: object,
) -> NgrokTunnel: ...
def default(session: Optional[NgrokSession] = None) -> NgrokTunnel: ...
def disconnect(url: Optional[str] = None) -> None: ...
def fd(session: Optional[NgrokSession] = None) -> int: ...
def getsockname(session: Optional[NgrokSession] = None) -> str: ...
def kill() -> None: ...
def listen(
    server: Optional[Any] = None, tunnel: Optional[NgrokTunnel] = None
) -> NgrokTunnel: ...
def log_level(level: str = "INFO") -> None: ...
def pipe_name() -> str: ...
def werkzeug_develop(
    tunnel: Optional[NgrokTunnel] = None,
) -> Union[Awaitable[NgrokTunnel], NgrokTunnel]: ...

class NgrokTunnel:
    def close(self) -> Awaitable[None]: ...
    def forward(self, addr: str) -> Awaitable[None]: ...
    def forwards_to(self) -> str: ...
    def id(self) -> str: ...
    def labels(self) -> Mapping[str, str]: ...
    def metadata(self) -> str: ...
    def proto(self) -> str: ...
    def url(self) -> str: ...

class NgrokSession:
    def close(self) -> Awaitable[None]: ...
    def close_tunnel(self, id: str) -> Awaitable[None]: ...
    def get_tunnels(self) -> List[NgrokTunnel]: ...
    def http_endpoint(self) -> NgrokHttpTunnelBuilder: ...
    def labeled_endpoint(self) -> NgrokLabeledTunnelBuilder: ...
    def tcp_endpoint(self) -> NgrokTcpTunnelBuilder: ...
    def tls_endpoint(self) -> NgrokTlsTunnelBuilder: ...

class NgrokSessionBuilder:
    def authtoken(self, authtoken: str) -> NgrokSessionBuilder: ...
    def authtoken_from_env(self) -> NgrokSessionBuilder: ...
    def ca_cert(self, cert_bytes: bytearray) -> NgrokSessionBuilder: ...
    def client_info(
        self, client_type: str, version: str, comments: Optional[str] = None
    ) -> NgrokSessionBuilder: ...
    def connect(self) -> Awaitable[NgrokSession]: ...
    def handle_disconnection(
        self, handler: Callable[[str, str]]
    ) -> NgrokSessionBuilder: ...
    def handle_heartbeat(self, handler: Callable[[int]]) -> NgrokSessionBuilder: ...
    def handle_restart_command(self, handler: Callable[[]]) -> NgrokSessionBuilder: ...
    def handle_stop_command(self, handler: Callable[[]]) -> NgrokSessionBuilder: ...
    def handle_update_command(
        self, handler: Callable[[str, str]]
    ) -> NgrokSessionBuilder: ...
    def heartbeat_interval(self, heartbeat_interval: int) -> NgrokSessionBuilder: ...
    def heartbeat_tolerance(self, heartbeat_tolerance: int) -> NgrokSessionBuilder: ...
    def metadata(self, metadata: str) -> NgrokSessionBuilder: ...
    def server_addr(self, server_addr: str) -> NgrokSessionBuilder: ...

class NgrokHttpTunnelBuilder:
    def allow_cidr(self, cidr: str) -> NgrokHttpTunnelBuilder: ...
    def basic_auth(self, username: str, password: str) -> NgrokHttpTunnelBuilder: ...
    def circuit_breaker(self, circuit_breaker: float) -> NgrokHttpTunnelBuilder: ...
    def compression(self) -> NgrokHttpTunnelBuilder: ...
    def deny_cidr(self, cidr: str) -> NgrokHttpTunnelBuilder: ...
    def domain(self, domain: str) -> NgrokHttpTunnelBuilder: ...
    def forwards_to(self, forwards_to: str) -> NgrokHttpTunnelBuilder: ...
    def listen(self) -> Awaitable[NgrokTunnel]: ...
    def listen_and_forward(self, url: str) -> Awaitable[NgrokTunnel]: ...
    def listen_and_serve(self, server: Any) -> Awaitable[NgrokTunnel]: ...
    def metadata(self, metadata: str) -> NgrokHttpTunnelBuilder: ...
    def mutual_tlsca(self, mutual_tlsca: bytearray) -> NgrokHttpTunnelBuilder: ...
    def oauth(
        self,
        provider: str,
        allow_emails: Optional[str] = None,
        allow_domains: Optional[str] = None,
        scopes: Optional[str] = None,
    ) -> NgrokHttpTunnelBuilder: ...
    def oidc(
        self,
        issuer_url: str,
        client_id: str,
        client_secret: str,
        allow_emails: Optional[str] = None,
        allow_domains: Optional[str] = None,
        scopes: Optional[str] = None,
    ) -> NgrokHttpTunnelBuilder: ...
    def proxy_proto(self, proxy_proto: str) -> NgrokHttpTunnelBuilder: ...
    def remove_request_header(self, name: str) -> NgrokHttpTunnelBuilder: ...
    def remove_response_header(self, name: str) -> NgrokHttpTunnelBuilder: ...
    def request_header(self, name: str, value: str) -> NgrokHttpTunnelBuilder: ...
    def response_header(self, name: str, value: str) -> NgrokHttpTunnelBuilder: ...
    def scheme(self, scheme: str) -> NgrokHttpTunnelBuilder: ...
    def webhook_verification(
        self, provider: str, secret: str
    ) -> NgrokHttpTunnelBuilder: ...
    def websocket_tcp_conversion(self) -> NgrokHttpTunnelBuilder: ...

class NgrokLabeledTunnelBuilder:
    def label(self, label: str, value: str) -> NgrokLabeledTunnelBuilder: ...
    def listen(self) -> Awaitable[NgrokTunnel]: ...
    def listen_and_forward(self, url: str) -> Awaitable[NgrokTunnel]: ...
    def listen_and_serve(self, server: Any) -> Awaitable[NgrokTunnel]: ...
    def metadata(self, metadata: str) -> NgrokLabeledTunnelBuilder: ...

class NgrokTcpTunnelBuilder:
    def allow_cidr(self, cidr: str) -> NgrokTcpTunnelBuilder: ...
    def deny_cidr(self, cidr: str) -> NgrokTcpTunnelBuilder: ...
    def forwards_to(self, forwards_to: str) -> NgrokTcpTunnelBuilder: ...
    def listen(self) -> Awaitable[NgrokTunnel]: ...
    def listen_and_forward(self, url: str) -> Awaitable[NgrokTunnel]: ...
    def listen_and_serve(self, server: Any) -> Awaitable[NgrokTunnel]: ...
    def metadata(self, metadata: str) -> NgrokTcpTunnelBuilder: ...
    def proxy_proto(self, proxy_proto: str) -> NgrokTcpTunnelBuilder: ...
    def remote_addr(self, remote_addr: str) -> NgrokTcpTunnelBuilder: ...

class NgrokTlsTunnelBuilder:
    def allow_cidr(self, cidr: str) -> NgrokTlsTunnelBuilder: ...
    def deny_cidr(self, cidr: str) -> NgrokTlsTunnelBuilder: ...
    def domain(self, domain: str) -> NgrokTlsTunnelBuilder: ...
    def forwards_to(self, forwards_to: str) -> NgrokTlsTunnelBuilder: ...
    def listen(self) -> Awaitable[NgrokTunnel]: ...
    def listen_and_forward(self, url: str) -> Awaitable[NgrokTunnel]: ...
    def listen_and_serve(self, server: Any) -> Awaitable[NgrokTunnel]: ...
    def metadata(self, metadata: str) -> NgrokTlsTunnelBuilder: ...
    def mutual_tlsca(self, mutual_tlsca: bytearray) -> NgrokTlsTunnelBuilder: ...
    def proxy_proto(self, proxy_proto: str) -> NgrokTlsTunnelBuilder: ...
    def termination(
        self, cert_pem: bytearray, key_pem: bytearray
    ) -> NgrokTlsTunnelBuilder: ...
